import enum
from dataclasses import dataclass
from enum import Enum
from typing import Dict, Tuple

from src.data.atlas import Anim, SpriteID


@dataclass
class Parallax:
    left: bool
    """Whether the image is the left one of the two images required to fill the screen"""
    speed: float
    """Speed at which the image moves in pixels per seconds"""


class Animation:
    def __init__(self, anim: Anim, frame_duration=0.1):
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
        self.index = (self.index + n) % len(self.anim)

    def replace(self, new_anim: Anim, frame_duration=None):
        self.__init__(new_anim, frame_duration or self.frame_duration)

    @property
    def cur_sprite_id(self):
        return self.anim[self.index]


@dataclass
class StateToAnimation:
    """A mapping from the states of the entity to the corresponding Anim."""

    state_to_animation: Dict["State", Anim]


class Flip(enum.IntFlag):
    NONE = 0
    VERT = 1
    HORI = 2
    BOTH = 4


@dataclass
class Sprite:
    id: SpriteID
    flip: Flip = Flip.NONE


class Camera:
    """
    The game's 2D camera. The coordinate system has the same axis
    as the usual R² plane - ie. increase right and up.

    Actual conversion between screen coords and opengl view is in
    the vertex shader.
    """

    center: [float, float]
    size: [float, float]

    def __init__(self, center, size):
        self.center = list(center)
        self.size = list(size)

    def as_vec4(self):
        return (*self.center, *self.size)

    @property
    def left(self):
        return self.center[0] - self.size[0] / 2

    @left.setter
    def left(self, value):
        self.center[0] = value + self.size[0] / 2

    @property
    def right(self):
        return self.center[0] + self.size[0] / 2

    @right.setter
    def right(self, value):
        self.center[0] = value - self.size[0] / 2

    @property
    def top(self):
        return self.center[1] + self.size[1] / 2

    @top.setter
    def top(self, value):
        self.center[1] = value - self.size[1] / 2

    @property
    def bottom(self):
        return self.center[1] - self.size[1] / 2

    @bottom.setter
    def bottom(self, value):
        self.center[1] = value + self.size[1] / 2
