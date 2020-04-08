"""
All the systems needed to render the game with moderngl.
"""

from src.esper import ProcessorBundle
from .animation_system import AnimationSystem
from .draw_sprites_system import DrawSpriteSystem
from .fog_system import FogSystem
from .move_camera_system import MoveCameraSystem
from .parallax_system import ParallaxSystem
from .select_animation_system import SelectAnimationSystem


class RenderBundle(ProcessorBundle):
    """An aggregate of systems to render the game with moderngl."""

    def __init__(self, window):
        super().__init__()

        self.add_processor(MoveCameraSystem(), 4)
        self.add_processor(SelectAnimationSystem(), 3)
        self.add_processor(ParallaxSystem(), 2)
        self.add_processor(AnimationSystem(), 2)
        self.add_processor(DrawSpriteSystem(window.ctx, window), 1)
        self.add_processor(FogSystem(window.ctx), 0)
