import shapely
from shapely import Point

from light_man.models import Room
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
import numpy as np

__all__ = ["find_optimal_positions_of_lights"]


def find_optimal_positions_of_lights(room: Room, n_rows: int, n_cols: int) -> list[Point]:
    light_geoms = []
    bad_lights = []

    room_points = tuple(room.dimensions.exterior.coords)
    for i in range(n_rows):
        for j in range(n_cols):
            x = (i + 0.5) * room_points[1][0] / n_rows
            y = (j + 0.5) * room_points[1][1] / n_cols
            light_geoms.append(shapely.Point(x, y))

    for light in light_geoms:
        for beam in room.beams:
            if beam.contains(light):
                bad_lights.append(light)
                print("Lights overlap with beams")
                break

    good_lights = [light for light in light_geoms if light not in bad_lights]

    # Create the distance field
    x = np.linspace(room.dimensions.bounds[0], room.dimensions.bounds[2], 100)
    y = np.linspace(room.dimensions.bounds[1], room.dimensions.bounds[3], 100)
    x, y = np.meshgrid(x, y)

    illuminance_factor = 1
    min_distance = 0.1
    illuminance_field = np.zeros_like(x)
    for light in good_lights:
        x_distance = light.x - x
        y_distance = light.y - y
        distance = np.sqrt(x_distance ** 2 + y_distance ** 2)
        distance = np.maximum(distance, min_distance)
        illuminance = illuminance_factor / (distance ** 2)
        illuminance_field += illuminance

    fig, ax = plt.subplots()
    ax.contourf(x, y, np.log10(illuminance_field), cmap="viridis")

    ax.plot(*room.dimensions.exterior.xy, color="black")
    for beam_geom in room.beams:
        ax.plot(*beam_geom.exterior.xy, color="brown")

    for light in good_lights:
        plt.plot(*light.buffer(1).exterior.xy, color="yellow", alpha=0.6)
        plt.plot(*light.buffer(0.2).exterior.xy, color="blue")
    for light in bad_lights:
        plt.plot(*light.buffer(0.2).exterior.xy, color="red")
    plt.show()

    return good_lights


def is_c_within_ab(a: Point, d: Point, m: Point):
    if m.x < min(a.x, d.x) or m.x > max(a.x, d.x) or m.y < min(a.y, d.y) or m.y > max(a.y, d.y):
        return False
    return True
