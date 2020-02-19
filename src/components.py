"""
This files contains all the components of Follow the Light.

They are only data structures with no logic,
since the logic is performed by the systems.
"""
from dataclasses import dataclass


@dataclass
class Pos:
    x: float
    y: float
    z: float

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z