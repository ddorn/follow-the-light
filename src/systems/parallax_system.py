import esper

from src import atlas
from src.atlas import Sprite
from src.components import Parallax, Pos


class ParallaxSystem(esper.Processor):
    world: esper.World

    def process(self, *args, **kwargs):
        camera = kwargs["camera"]
        time = kwargs["time"]

        for e, (parallax, sprite, pos) in self.world.get_components(
            Parallax, Sprite, Pos
        ):
            x = camera.left + (parallax.speed * time) % atlas.RECTS[sprite.value][6]
            if parallax.left:
                pos.x = x - atlas.RECTS[sprite.value][6]
            else:
                pos.x = x
