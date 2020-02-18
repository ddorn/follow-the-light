import struct

import esper
import moderngl
import moderngl_window
import numpy as np

from src import shaders, shapes, atlas
from src.atlas import Sprite


class DrawSpriteSystem(esper.Processor):
    def __init__(self, ctx: moderngl.Context, window_conf: moderngl_window.WindowConfig):
        self.prog = shaders.load_shader("simple", ctx)

        # Load the texture with nearest filter
        atlas_path = "atlas.png"
        tex = window_conf.load_texture_2d(atlas_path, flip=True)
        self.sampler = ctx.sampler(filter=(moderngl.NEAREST, moderngl.NEAREST), texture=tex)
        tex.use()

        vertices, indices = shapes.get_rect(-1, -1, 2, 2)

        # Set up the buffers
        self.vbo = ctx.buffer(vertices.astype('f4').flatten().tobytes())
        self.ibo = ctx.buffer(indices.astype('i4').tobytes())
        # Set up the atlas coordinates
        self.prog['rects'].write(np.array(atlas.RECTS).astype('f4').tobytes())

        # Set up the images ids buffer. TODO: leave that to components
        images = [
            ((i + 1) / 8 - 1., sprite.value) for (i, sprite) in
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
        images = struct.pack("fi" * len(images), *[x for p in images for x in p])
        self.images = ctx.buffer(images)

        # The vao to draw actually things
        self.vao = ctx.vertex_array(
            self.prog,
            [
                (self.vbo, "3f4 2f4 /v", "vert", "tex_coord"),
                (self.images, "f4 u4 /i", "z", "sprite_id")
            ],
            self.ibo)

    def process(self, *args, **kwargs):
        self.prog['time'].value = kwargs.get('time', 0.)
        self.sampler.use()

        sprite_count = self.images.size // 8
        print("Sprites:", sprite_count)
        self.vao.render(instances=sprite_count)
