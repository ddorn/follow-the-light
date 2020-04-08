from src.render.components import Animation
from src.esper import Processor, World
from src.data.atlas import Sprite


class AnimationSystem(Processor):
    world: World

    def process(self, *args, **kwargs):
        # dt is negative on the first frame
        dt = max(kwargs["frame_time"], 0.0)

        anim: Animation
        for e, anim in self.world.get_component(Animation):
            if anim.update(dt):
                anim.advance(1)
                self.world.add_component(e, Sprite(anim.anim.value[anim.index]))
