from shapely import Point
import shapely

from light_man import Room
import collections

__all__ = ["find_optimal_positions_of_lights"]


def find_optimal_positions_of_lights(room: Room, n_rows: int, n_cols : int) -> list[Point]:

    light_geoms = []
    bad_lights = []

    room_points = tuple(room.dimensions.exterior.coords)
    print(room_points)
    for i in range(n_rows):
        for j in range(n_cols):
            x = (i + 0.5)* room_points[1][0] / n_rows
            y = (j+ 0.5) * room_points[1][1] / n_cols
            light_geoms.append(shapely.Point(x, y))

    for light in light_geoms:
        for beam in room.beams:
            if beam.contains(light):
                bad_lights.append(light);
                print("Lights overlap with beams")
                break;    
          
    result = collections.Counter(light_geoms) or collections.Counter(bad_lights)
    good_lights = list(result.elements())   
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(*room.dimensions.exterior.xy, color="black")
    for beam_geom in room.beams:
        ax.plot(*beam_geom.exterior.xy, color="brown")
    x, y = [light.x for light in good_lights], [light.y for light in good_lights]
    ax.scatter(x, y, color="blue")
    x, y = [light.x for light in bad_lights], [light.y for light in bad_lights]
    ax.scatter(x, y, color="red")
    plt.show()

def is_c_within_ab(a: Point, d: Point, m: Point):
    if m.x < min(a.x, d.x) or m.x > max(a.x, d.x) or m.y < min(a.y, d.y) or m.y > max(a.y, d.y):
        return False
    return True;

