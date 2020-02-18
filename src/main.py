#!/usr/bin/env python3
import struct

import moderngl
import moderngl_window
import numpy as np

from src import shaders, shapes, atlas
from src.paths import ASSETS_DIR
from src.atlas import Sprite


class Window(moderngl_window.WindowConfig):
    gl_version = (3, 3)
    window_size = (384, 216)
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

        images = [
            ((i+1)/8 - 1.,  sprite.value) for (i, sprite) in
                enumerate([
                    Sprite.BG_LAYER_0_SKY,
                    Sprite.BG_LAYER_1_CLOUDS,
                    Sprite.BG_LAYER_2_CLOUND_LONELY,
                    Sprite.BG_LAYER_3_MOUNTAINS,
                    Sprite.BG_LAYER_4_DARK_LOW_CLOUDS,
                    Sprite.BG_LAYER_5_LOW_CLOUDS,
                    Sprite.BG_LAYER_6_LIGHT_CLOUDS,
                ])
            ]

        # images = np.array([2])
        print(images)
        images = struct.pack("fi" * len(images), *[x for p in images for x in p])
        print(images)
        self.images = self.ctx.buffer(images)
        self.vao = self.ctx.vertex_array(
            self.prog,
            [
                (vbo, "3f4 2f4 /v", "vert", "tex_coord"),
                (self.images, "f4 u4 /i", "z", "sprite_id")
            ],
            ibo)

    def render(self, time: float, frame_time: float):
        self.prog['time'].value = time
        self.sampler.use()

        sprite_count = self.images.size // 8
        print("Sprites:", sprite_count)
        self.vao.render(instances=sprite_count)


if __name__ == "__main__":
    moderngl_window.run_window_config(Window)
