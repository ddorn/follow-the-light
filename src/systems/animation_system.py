from esper import Processor, World

from src.atlas import Sprite
from src.components import Animation


class AnimationSystem(Processor):
    world: World

    def process(self, *args, **kwargs):
        # dt is negative on the first frame
        dt = max(kwargs['frame_time'], 0.0)

        anim: Animation
        for e, (sprite, anim) in self.world.get_components(Sprite, Animation):
            anim.dt += dt
            if anim.dt >= anim.frame_duration:
                anim.dt -= anim.frame_duration
                self.world.add_component(e, sprite.next())
