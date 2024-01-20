from typing import List

import shapely
from pydantic import BaseModel

__all__ = ["Point", "Beam", "Room", "Rectangle"]


class Point(BaseModel):
    x: float
    y: float

    def to_shapely(self):
        return shapely.geometry.Point(self.x, self.y)


class Rectangle(BaseModel):
    p1: Point
    p2: Point

    @property
    def width(self):
        return abs(self.p1.x - self.p2.x)

    @property
    def height(self):
        return abs(self.p1.y - self.p2.y)

    def to_shapely(self):
        return shapely.geometry.box(
            self.p1.x,
            self.p1.y,
            self.p2.x,
            self.p2.y,
        )


class Beam(BaseModel):
    geometry: Rectangle


class Room(BaseModel):
    geometry: Rectangle
    beams: List[Beam]
