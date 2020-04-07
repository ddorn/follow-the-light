

from src import esper
from src.graphism import atlas
from src.graphism.atlas import Sprite
from src.components import Parallax, Pos


class ParallaxSystem(esper.Processor):
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
