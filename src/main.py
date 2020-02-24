#!/usr/bin/env python3

import esper
import moderngl
import moderngl_window

from src import systems
from src.atlas import Sprite
from src.camera import Camera
from src.components import Pos, Parallax, Player
from src.paths import ASSETS_DIR


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
        self.world.add_processor(systems.DrawSpriteSystem(self.ctx, self), 3)
        self.world.add_processor(systems.MoveCameraSystem(), 1)
        self.world.add_processor(systems.ParallaxSystem(), 2)
        self.init_background()
        self.init_camera()
        self.init_player()

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
            for side in (True, False):
                self.world.create_entity(
                    sprite, Pos(0, 0, i / 10), Parallax(side, -i * 5)
                )

    def init_camera(self):
        size = self.window_size
        self.camera = Camera((size[0] / 2, size[1] / 2), size)

    def init_player(self):
        size = self.window_size
        self.world.create_entity(Player(), Pos(size[0] / 2, size[1] / 2, 0),
                                 Sprite(Sprite.ADVENTURER_IDLE_00))

    def render(self, time: float, frame_time: float):
        self.world.process(
            ctx=self.ctx,
            time=time,
            frame_time=frame_time,
            camera=self.camera,
            screen_size=self.wnd.size,
        )


if __name__ == "__main__":
    moderngl_window.run_window_config(Window)
