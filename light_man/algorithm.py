import shapely

from light_man import Point, Room

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


def find_optimal_positions_of_lights(room: Room, n_lights: int) -> list[Point]:
    room_geom, beam_geoms = convert_room_to_shapely_objects(room)
    light_geoms = []

    for i in range(n_lights):
        x = room.dimensions.p1.x + (i + 0.5) * room.dimensions.width / n_lights
        y = room.dimensions.p1.y + (i + 0.5) * room.dimensions.height / n_lights
        light_geoms.append(shapely.geometry.Point(x, y))

    # plot the geometry
    import matplotlib.pyplot as plt

    fig, ax = plt.subplots()
    ax.plot(*room_geom.exterior.xy, color="black")
    for beam_geom in beam_geoms:
        ax.plot(*beam_geom.exterior.xy, color="red")
    x, y = [light.x for light in light_geoms], [light.y for light in light_geoms]
    ax.scatter(x, y, color="blue")
    plt.show()
