from src import esper
from src.data import atlas
from src.logic.components import Pos, Player
from src.render.components import Parallax, Sprite


class ParallaxSystem(esper.Processor):
    def process(self, *args, **kwargs):
        camera = kwargs["camera"]

        # Find the position of the player
        ppos = None
        for _, (ppos, _) in self.world.get_components(Pos, Player):
            break

        for e, (parallax, sprite, pos) in self.world.get_components(
            Parallax, Sprite, Pos
        ):

            x = (
                camera.center[0]
                + (parallax.speed * ppos.x) % atlas.RECTS[sprite.id.value][6]
            )
            if parallax.left:
                pos.x = x - atlas.RECTS[sprite.id.value][6]
            else:
                pos.x = x
