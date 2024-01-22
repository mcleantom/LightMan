from typing import List

import shapely

__all__ = ["Room"]


class Room:
    def __init__(self, dimensions: shapely.geometry.box, beams: List[shapely.geometry.box]):
        self.dimensions = dimensions
        self.beams = beams
