from pydantic import BaseModel
from typing import List
import numpy as np
__all__ = ["Point", "Beam", "Room", "Rectangle"]


class Point(BaseModel):
    x: float
    y: float

    def __sub__(self, other):
        return Point(x = self.x - other.x, y = self.y - other.y)
    
    def dot(self, other):
        return np.dot([self.x, self.y], [other.x, other.y])
    
    def __hash__(self):
        return hash(self.x)^hash(self.y)


class Rectangle(BaseModel):
    p1: Point
    p2: Point

    @property
    def width(self):
        return abs(self.p1.x - self.p2.x)

    @property
    def height(self):
        return abs(self.p1.y - self.p2.y)


class Beam(BaseModel):
    dimensions: Rectangle


class Room(BaseModel):
    dimensions: Rectangle
    beams: List[Beam]
