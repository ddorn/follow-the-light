from src.esper import Processor
from src.logic.components import Facing
from src.render.components import Sprite, Flip


class FlipSpriteSystem(Processor):
    """Flip the sprites according to the Facing of the entity."""

    def process(self, *args, **kwargs):
        for e, (facing, sprite) in self.world.get_components(Facing, Sprite):
            if facing.left:
                sprite.flip = Flip.HORI
            else:
                sprite.flip = Flip.NONE
