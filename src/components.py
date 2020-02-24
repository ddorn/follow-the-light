"""
This files contains all the components of Follow the Light.

They are only data structures with no logic,
since the logic is performed by the systems.
"""
from dataclasses import dataclass

from src.atlas import Anim


@dataclass
class Pos:
    x: float
    y: float
    z: float

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __add__(self, other):
        x, y, z = other
        return Pos(self.x + x, self.y + y, self.z + z)


@dataclass
class Parallax:
    left: bool
    """Whether the image is the left one of the two images required to fill the screen"""
    speed: float
    """Speed at which the image moves in pixels per seconds"""


class Player:
    pass


class Animation:
    def __init__(self, anim: Anim, frame_duration=15 / 60):
        self.dt = 0.0
        self.frame_duration = frame_duration
        self.index = 0
        self.anim = anim

    def update(self, frame_time: float):
        """True if the animation should go to the next frame"""
        self.dt += frame_time
        if self.dt >= self.frame_duration:
            self.dt -= self.frame_duration
            return True
        return False

    def advance(self, n=1):
        self.index = (self.index + n) % len(self.anim.value)

