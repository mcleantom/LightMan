from pydantic import BaseModel

__all__ = ["Point", "Beam", "Room", "Rectangle"]


class Point(BaseModel):
    x: float
    y: float


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
    beams: list[Beam]
