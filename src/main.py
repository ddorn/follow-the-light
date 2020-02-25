#!/usr/bin/env python3

import esper
import moderngl
import moderngl_window

from src import systems
from src.atlas import Sprite, Anim
from src.camera import Camera
from src.components import Pos, Parallax, Player, Animation
from src.paths import ASSETS_DIR


class Window(moderngl_window.WindowConfig):
    gl_version = (3, 3)
    window_size = (650, 650*9//16)
    # window_size = (384, 216)
    resource_dir = ASSETS_DIR
    title = "Follow the light"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        # Set up options on the opengl context
        self.ctx.enable(moderngl.BLEND)
        # self.ctx.enable(moderngl.DEPTH_TEST)

        # Set up the world for all our entities
        self.world = esper.World()
        # High numbers first
        self.world.add_processor(systems.MoveCameraSystem(), 3)
        self.world.add_processor(systems.ParallaxSystem(), 2)
        self.world.add_processor(systems.AnimationSystem(), 2)
        self.world.add_processor(systems.DrawSpriteSystem(self.ctx, self), 1)
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

        layers = [
            Sprite.BG_FOREST_0_SKY,
            Sprite.BG_FOREST_1_SHADOWS,
            Sprite.BG_FOREST_2_DARK_SHADOW,
            Sprite.BG_FOREST_3_LIGHTS,
            Sprite.BG_FOREST_4_TREES,
            Sprite.BG_FOREST_5_BIGGER_TREES,
            Sprite.BG_FOREST_5_MORE_TREES,
            Sprite.BG_FOREST_6_LIGHTS,
            Sprite.BG_FOREST_6_LEAVES,
            Sprite.BG_FOREST_7_GRASS,
            Sprite.BG_FOREST_8_DARK_GRASS,
        ]

        for i, sprite in enumerate(layers):
            for side in (True, False):
                self.world.create_entity(
                    sprite, Pos(0, 0, i / len(layers) - 1), Parallax(side, -i * 5)
                )

        for i, sprite in enumerate(layers):
            for side in (True, False):
                self.world.create_entity(
                    sprite, Pos(0, 0, i / 7 - 1), Parallax(side, -i * 5)
                )

    def init_camera(self):
        size = self.window_size
        self.camera = Camera((size[0] / 2, size[1] / 2), size)

    def init_player(self):
        size = self.window_size
        self.world.create_entity(
            Player(),
            Pos(size[0] / 2, size[1] / 2, 0),
            Animation(Anim.ADVENTURER_ATTACK2, 5 / 60),
        )

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
