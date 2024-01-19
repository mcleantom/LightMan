from enum import Enum

from pydantic import BaseModel

__all__ = ["Point", "EOrientation", "Beam", "Room"]


class Point(BaseModel):
    x: float
    y: float


class EOrientation(Enum):
    HORIZONTAL = 0
    VERTICAL = 1


class Beam(BaseModel):
    position: Point
    orientation: EOrientation
    width: float


class Room(BaseModel):
    width: float
    height: float
    beams: list[Beam]
