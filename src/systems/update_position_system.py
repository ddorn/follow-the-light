from esper import Processor, World

from src.components import Pos, Vel


class UpdatePositionSystem(Processor):
    """
    This system converts the inputs into buffs for entities.
    """

    world: World

    def process(self, *args, frame_time, **kwargs):
        for e, (pos, vel) in self.world.get_components(Pos, Vel):
            pos += vel * frame_time
