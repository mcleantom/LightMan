import shapely

from light_man import Point, Room
import collections

__all__ = ["find_optimal_positions_of_lights"]


def convert_room_to_shapely_objects(room: Room):
    room_shapely = shapely.geometry.box(
        room.dimensions.p1.x,
        room.dimensions.p1.y,
        room.dimensions.p2.x,
        room.dimensions.p2.y,
    )
    beams_shapely = [
        shapely.geometry.box(
            beam.dimensions.p1.x,
            beam.dimensions.p1.y,
            beam.dimensions.p2.x,
            beam.dimensions.p2.y,
        )
        for beam in room.beams
    ]
    return room_shapely, beams_shapely


def find_optimal_positions_of_lights(room: Room, n_rows: int, n_cols : int) -> list[Point]:
    room_geom, beam_geoms = convert_room_to_shapely_objects(room)
    light_geoms = []
    bad_lights = []

    for i in range(n_rows):
        for j in range(n_cols):
            x = room.dimensions.p1.x + (i + 0.5)* room.dimensions.width / n_rows
            y = room.dimensions.p1.y + (j+ 0.5) * room.dimensions.height / n_cols
            light_geoms.append(shapely.Point(x, y))

    for light in light_geoms:
        for beam in room.beams:
            if is_c_within_ab(beam.dimensions.p1, beam.dimensions.p2, light):
                bad_lights.append(light);
                print("Lights overlap with beams")
                break;
                
    result = collections.Counter(light_geoms) or collections.Counter(bad_lights)
    good_lights = list(result.elements())   
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(*room_geom.exterior.xy, color="black")
    for beam_geom in beam_geoms:
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

