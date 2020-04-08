from src.esper import Processor
from src.logic.components import Facing, Vel


class FacingSystem(Processor):
    """
    This system updates the Facing according to the velocity.
    """

    def process(self, *args, **kwargs):
        for e, (facing, vel) in self.world.get_components(Facing, Vel):
            if vel.x > 0:
                facing.right = True
            elif vel.x < 0:
                facing.left = True
