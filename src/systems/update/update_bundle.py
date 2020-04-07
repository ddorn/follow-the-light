from src.esper import ProcessorBundle
from src.systems.update.buffs_system import BuffSystem
from src.systems.update.collision_system import CollisionSystem
from src.systems.update.input_system import InputSystem
from src.systems.update.move_camera_system import MoveCameraSystem
from src.systems.update.state_machine_system import StateMachineSystem
from src.systems.update.update_position_system import UpdatePositionSystem


class UpdateBundle(ProcessorBundle):
    def __init__(self):
        super().__init__()

        self.add_processor(BuffSystem(), 5)
        self.add_processor(InputSystem(), 4)
        self.add_processor(StateMachineSystem(), 3)
        self.add_processor(UpdatePositionSystem(), 2)
        self.add_processor(CollisionSystem(), 1)
        self.add_processor(MoveCameraSystem(), 0)
