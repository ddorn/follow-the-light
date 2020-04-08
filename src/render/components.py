from dataclasses import dataclass
from typing import Dict

from src.data.atlas import Anim


@dataclass
class Parallax:
    left: bool
    """Whether the image is the left one of the two images required to fill the screen"""
    speed: float
    """Speed at which the image moves in pixels per seconds"""


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

    def replace(self, new_anim: Anim, frame_duration=None):
        self.__init__(new_anim, frame_duration or self.frame_duration)


@dataclass
class StateToAnimation:
    """A mapping from the states of the entity to the corresponding Anim."""
    state_to_animation: Dict["State", Anim]


@dataclass
class Camera:
    """
    The game's 2D camera. The coordinate system has the same axis
    as the usual R² plane - ie. increase right and up.

    Actual conversion between screen coords and opengl view is in
    the vertex shader.
    """

    center: (float, float)
    size: (float, float)

    def as_vec4(self):
        return self.center + self.size

    @property
    def left(self):
        return self.center[0] - self.size[0] / 2