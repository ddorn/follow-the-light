import esper

from src.components import Player, Pos
from src.locals.constants import PLAYER_HORIZONTALS_SPEED


class PlayerHorizontalMoveSystem(esper.Processor):
    world: esper.World

    def process(self, *args, **kwargs):
        inputs = kwargs["inputs"]
        for e, (player, pos) in self.world.get_components(Player, Pos):
            pos.x += inputs["horizontal"].value * PLAYER_HORIZONTALS_SPEED
