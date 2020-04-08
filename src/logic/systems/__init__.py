"""
All the systems needed for the logic of the game.
"""

from src.esper import ProcessorBundle
from .buffs_system import BuffSystem
from .collision_system import CollisionSystem
from .facing_system import FacingSystem
from .input_system import InputSystem
from .state_machine_system import StateMachineSystem
from .update_position_system import UpdatePositionSystem


class LogicBundle(ProcessorBundle):
    """An aggregate of systems that define the whole logic."""

    def __init__(self):
        super().__init__()

        self.add_processor(BuffSystem(), 5)
        self.add_processor(InputSystem(), 4)
        self.add_processor(StateMachineSystem(), 3)
        self.add_processor(UpdatePositionSystem(), 2)
        self.add_processor(CollisionSystem(), 1)
        self.add_processor(FacingSystem())
