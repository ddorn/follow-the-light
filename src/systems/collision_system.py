
from src.esper import Processor, World
from src.components import Pos, Vel, Collisions


class CollisionSystem(Processor):
    """
    This system converts the inputs into buffs for entities.
    """

    world: World

    def process(self, *args, frame_time, **kwargs):
        for e, (pos, hit) in self.world.get_components(Pos, Collisions):
            hit.bottom = pos.y < 64
