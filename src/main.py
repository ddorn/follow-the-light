#!/usr/bin/env python3

import moderngl
import moderngl_window
import numpy as np

from src import shaders, shapes, atlas
from src.paths import ASSETS_DIR
from src.atlas import Sprite


class Window(moderngl_window.WindowConfig):
    gl_version = (3, 3)
    window_size = (800, 500)
    resource_dir = ASSETS_DIR
    title = "Follow the light"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        print("Follow the light !")
        self.ctx.enable(moderngl.BLEND)
        # self.ctx.blend_func = (moderngl.SRC_ALPHA, moderngl.DST_ALPHA)
        # self.ctx.enable(moderngl.DEPTH_TEST)

        self.prog = shaders.load_shader("simple", self.ctx)
        vertices, indices = shapes.get_rect(-1, -1, 2, 2)

        vbo = self.ctx.buffer(vertices.astype('f4').flatten().tobytes())
        ibo = self.ctx.buffer(indices.astype('i4').tobytes())

        atlas_path = "atlas.png"
        tex = self.load_texture_2d(atlas_path, flip=True)
        self.sampler = self.ctx.sampler(filter=(moderngl.NEAREST, moderngl.NEAREST), texture=tex)
        tex.use()

        self.prog['rects'].write(np.array(atlas.RECTS).astype('f4').tobytes())
        # self.prog['rects'].value = atlas.RECTS

        images = np.array(
            [
                sprite.value for sprite in
                reversed([
                    Sprite.BG_LAYER_6_LIGHT_CLOUDS,
                    Sprite.BG_LAYER_5_LOW_CLOUDS,
                    Sprite.BG_LAYER_4_DARK_LOW_CLOUDS,
                    Sprite.BG_LAYER_3_MOUNTAINS,
                    Sprite.BG_LAYER_2_CLOUND_LONELY,
                    Sprite.BG_LAYER_1_CLOUDS,
                    Sprite.BG_LAYER_0_SKY,
                ])
            ]
        )

        # images = np.array([2])
        print(images)
        self.images = self.ctx.buffer(images.astype('i4').tobytes())
        self.vao = self.ctx.vertex_array(
            self.prog,
            [
                (vbo, "2f4 2f4 /v", "vert", "tex_coord"),
                (self.images, "u4 /i", "sprite_id")
            ],
            ibo)

    def render(self, time: float, frame_time: float):
        self.prog['time'].value = time
        self.sampler.use()

        sprite_count = self.images.size // 4
        print("Sprites:", sprite_count)
        self.vao.render(instances=sprite_count)


if __name__ == "__main__":
    moderngl_window.run_window_config(Window)
