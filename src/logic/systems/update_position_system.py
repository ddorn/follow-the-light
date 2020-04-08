from src.logic.components import Pos, Vel
from src.esper import Processor


class UpdatePositionSystem(Processor):
    """
    This system converts the inputs into buffs for entities.
    """

    def process(self, *args, frame_time, **kwargs):
        for e, (pos, vel) in self.world.get_components(Pos, Vel):
            pos += vel * frame_time
