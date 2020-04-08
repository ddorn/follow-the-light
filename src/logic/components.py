"""
This files contains all the components of Follow the Light.

They are only data structures with no logic,
since the logic is performed by the systems.
"""
from collections import defaultdict
from dataclasses import dataclass


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

    def __mul__(self, a):
        return self.__class__(self.x * a, self.y * a, self.z * a)

    def __iadd__(self, other):
        x, y, z = other
        self.x += x
        self.y += y
        self.z += z
        return self


class Pos(Vec3):
    pass


class Vel(Vec3):
    pass


class Acc(Vec3):
    pass


class Player:
    pass


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


@dataclass
class Collisions:
    left: bool = False
    right: bool = False
    top: bool = False
    bottom: bool = False


