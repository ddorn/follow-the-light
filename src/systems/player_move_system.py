import esper

from src.components import Player, Pos
from src.locals.constants import PLAYER_SPEED


class PlayerMoveSystem(esper.Processor):
    world: esper.World

    def process(self, *args, inputs, **kwargs):

        for e, (player, pos) in self.world.get_components(Player, Pos):
            pos.x += inputs["hmove"].value * PLAYER_SPEED
            pos.y += inputs["vmove"].value * PLAYER_SPEED
