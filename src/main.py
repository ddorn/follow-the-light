#!/usr/bin/env python3
import struct

import esper
import moderngl
import moderngl_window
import numpy as np

from src import shaders, shapes, atlas, systems
from src.components import Pos
from src.paths import ASSETS_DIR
from src.atlas import Sprite


class Window(moderngl_window.WindowConfig):
    gl_version = (3, 3)
    window_size = (384, 216)
    resource_dir = ASSETS_DIR
    title = "Follow the light"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set up options on the opengl context
        self.ctx.enable(moderngl.BLEND)
        # self.ctx.enable(moderngl.DEPTH_TEST)

        # Set up the world for all our entities
        self.world = esper.World()
        self.world.add_processor(systems.DrawSpriteSystem(self.ctx, self))
        self.init_background()

    def init_background(self):
        layers = [
            Sprite.BG_LAYER_0_SKY,
            Sprite.BG_LAYER_1_CLOUDS,
            Sprite.BG_LAYER_2_CLOUND_LONELY,
            Sprite.BG_LAYER_3_MOUNTAINS,
            Sprite.BG_LAYER_4_DARK_LOW_CLOUDS,
            Sprite.BG_LAYER_5_LOW_CLOUDS,
            Sprite.BG_LAYER_6_LIGHT_CLOUDS,
        ]

        for i, sprite in enumerate(layers):
            self.world.create_entity(
                sprite,
                Pos(0, 0, i/10)
            )

    def render(self, time: float, frame_time: float):
        self.world.process(ctx=self.ctx, time=time, screen_size=self.window_size)


if __name__ == "__main__":
    moderngl_window.run_window_config(Window)
