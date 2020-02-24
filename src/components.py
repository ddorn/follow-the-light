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


@dataclass
class Parallax:
    left: bool
    """Whether the image is the left one of the two images required to fill the screen"""
    speed: float
    """Speed at which the image moves in pixels per seconds"""


class Player:
    pass


class Animation:
    dt: float
    frame_duration: float

    def __init__(self, frame_duration = 15/60):
        self.dt = 0.0
        self.frame_duration = frame_duration
