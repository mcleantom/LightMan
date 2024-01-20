from typing import List

import shapely

from light_man.models import Point, Room

__all__ = ["find_optimal_positions_of_lights"]


def find_optimal_positions_of_lights(room: Room, n_lights: int) -> List[Point]:
    room.geometry.to_shapely()
    [beam.geometry.to_shapely() for beam in room.beams]
    light_geoms = []

    for i in range(n_lights):
        x = room.geometry.p1.x + (i + 0.5) * room.geometry.width / n_lights
        y = room.geometry.p1.y + (i + 0.5) * room.geometry.height / n_lights
        light_geoms.append(shapely.geometry.Point(x, y))
