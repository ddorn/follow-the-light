from typing import Optional


from src.logic.components import Buffs, Vel, Collisions
from src.esper import World
from src.logic.constants import *
from src.logic.state_machine.base import State


__all__ = ["GroundedState", "FallState", "JumpState"]


class JumpState(State):
    def next_state(self, entity: int, world: World) -> Optional["State"]:
        buffs = world.component_for_entity(entity, Buffs)
        vel = world.component_for_entity(entity, Vel)
        colli = world.component_for_entity(entity, Collisions)

        if colli.bottom:
            return GroundedState()
        if buffs[VERTICAL_LOCK] or vel.y <= 0.0:
            return FallState()
        if not buffs[WANT_JUMP]:
            return FallState()
        return None

    def update(self, entity: int, world: World):
        buffs = world.component_for_entity(entity, Buffs)
        vel = world.component_for_entity(entity, Vel)

        vel.y = PLAYER_SPEED

        if buffs[WANT_LEFT] == buffs[WANT_RIGHT] or buffs[HORIZONTAL_LOCK]:
            vel.x = 0
        elif buffs[WANT_RIGHT]:
            vel.x = PLAYER_SPEED
        else:
            vel.x = -PLAYER_SPEED

        return None


class FallState(State):
    def next_state(self, entity: int, world: World) -> Optional["State"]:
        colli = world.component_for_entity(entity, Collisions)

        if colli.bottom:
            return GroundedState()
        return None

    def update(self, entity: int, world: World):
        buffs = world.component_for_entity(entity, Buffs)
        vel = world.component_for_entity(entity, Vel)

        if buffs[VERTICAL_LOCK]:
            vel.y = 0
        else:
            vel.y = -PLAYER_SPEED

        if buffs[WANT_LEFT] == buffs[WANT_RIGHT] or buffs[HORIZONTAL_LOCK]:
            vel.x = 0
        elif buffs[WANT_RIGHT]:
            vel.x = PLAYER_SPEED
        else:
            vel.x = -PLAYER_SPEED


class GroundedState(State):
    def next_state(self, entity: int, world: World) -> Optional["State"]:
        buffs = world.component_for_entity(entity, Buffs)
        colli = world.component_for_entity(entity, Collisions)

        if not colli.bottom:
            return FallState()

        if buffs[WANT_JUMP] and not buffs[VERTICAL_LOCK]:
            return JumpState()

        return None

    def update(self, entity: int, world: World):
        buffs = world.component_for_entity(entity, Buffs)
        vel = world.component_for_entity(entity, Vel)

        vel.y = 0
        if buffs[WANT_LEFT] == buffs[WANT_RIGHT] or buffs[HORIZONTAL_LOCK]:
            vel.x = 0
        elif buffs[WANT_RIGHT]:
            vel.x = PLAYER_SPEED
        else:
            vel.x = -PLAYER_SPEED
