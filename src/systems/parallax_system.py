import esper

from src.components import Parallax, Pos


class ParallaxSystem(esper.Processor):
    world: esper.World

    def process(self, *args, **kwargs):
        camera = kwargs["camera"]
        time = kwargs["time"]

        for e, (parallax, pos) in self.world.get_components(Parallax, Pos):
            x = camera.left + (parallax.speed * time) % camera.size[0]
            if parallax.left:
                pos.x = x - camera.size[0]
            else:
                pos.x = x
