"""
This files contains all the components of Follow the Light.

They are only data structures with no logic,
since the logic is performed by the systems.
"""
from collections import defaultdict
from dataclasses import dataclass

from src.graphism.atlas import Anim


@dataclass
class Vec3:
    x: float
    y: float
    z: float

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def __add__(self, other):
        x, y, z = other
        return self.__class__(self.x + x, self.y + y, self.z + z)


class Pos(Vec3):
    pass


class Vel(Vec3):
    pass


class Acc(Vec3):
    pass


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


class Buffs(defaultdict):
    """
    Buffs is a component that stores the time left for each buff.

    >>> buffs = Buffs()
    >>> buffs["invincible"] = 1.0  # One second of invicibility
    >>> buffs["no-attack"] += 0.1  # Add one second without attack

    When the time for a buff is 0.0, the buff is not active anymore,
    even though the entry is still there.
    """

    def __init__(self):
        super().__init__(float)
