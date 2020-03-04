import esper

from src.components import Player, Pos


class PlayerHorizontalMoveSystem(esper.Processor):
    world: esper.World

    def process(self, *args, **kwargs):
        inputs = kwargs["inputs"]
        for e, (player, pos) in self.world.get_components(Player, Pos):
            pos.x += inputs["horizontal"].value
