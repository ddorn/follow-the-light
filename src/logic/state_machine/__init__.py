"""
The state machine of the player.

This package describes all the states the player can be,
with the transitions and behavior of each state.
"""

from .movement_machine import GroundedState, JumpState, FallState