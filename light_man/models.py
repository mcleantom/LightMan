from pydantic import BaseModel
from typing import List
import shapely
import numpy as np
__all__ = ["Room"]

class Room:
    dimensions: shapely.geometry.box
    beams: List[shapely.geometry.box]

    def __init__(self, dimensions, beams):
        self.dimensions = dimensions
        self.beams = beams
