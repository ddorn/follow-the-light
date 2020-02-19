import struct

import esper
import moderngl
import moderngl_window
import numpy as np

from src import shaders, atlas
from src.atlas import Sprite
from src.components import Pos


class DrawSpriteSystem(esper.Processor):
    world: esper.World

    def __init__(
        self, ctx: moderngl.Context, window_conf: moderngl_window.WindowConfig
    ):
        self.prog = shaders.load_shader("texture", ctx)

        # Load the texture with nearest filter
        atlas_path = "atlas.png"
        tex = window_conf.load_texture_2d(atlas_path, flip=True)
        tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
        tex.use()

        # Set up the buffers
        self.vbo = ctx.buffer(reserve=1024)
        self.ibo = ctx.buffer(reserve=1024)

        # The vao to draw actually things
        self.vao = ctx.vertex_array(
            self.prog,
            [
                (self.vbo, "3f4 2f4 /v", "vert", "tex_coord"),
                # (self.images, "f4 u4 /i", "z", "sprite_id")
            ],
            self.ibo,
        )

    def process(self, *args, **kwargs):
        self.vbo.clear()
        self.ibo.clear()
        self.prog['camera'].value = kwargs['camera'].as_vec4()

        tex_size = atlas.TEX_WIDTH, atlas.TEX_HEIGHT
        screen_size = kwargs["screen_size"]
        indices = np.array([0, 1, 2, 0, 2, 3], dtype="i4")

        qte = 0
        for e, (sprite, pos) in self.world.get_components(Sprite, Pos):
            assert (
                qte + 1
            ) * 20 * 4 < 1024, "You have a lot of sprites now, good job ! You need bigger buffer though"

            # We compute the xyz coordinates of each point and the uv coordinate
            # in the texture
            i = sprite.value
            uvwh = atlas.RECTS[i * 4 : (i + 1) * 4]
            points = self.points(pos, uvwh, tex_size, screen_size)

            bytes = struct.pack("20f", *points)
            self.vbo.write(bytes, offset=qte * len(bytes))

            # The  indices are about the next four points we just wrote
            bytes = indices.tobytes()
            self.ibo.write(bytes, offset=qte * len(bytes))
            indices += 4

            qte += 1

        self.vao.render()

    def points(self, xyz, uvwh, tex_size, screen_size):
        x, y, z = xyz
        u, v, w, h = uvwh
        tw, th = tex_size
        sw, sh = screen_size

        points = [
            (
                x + w * dx,  # x in -1..1 (TODO: Camera in shader)
                y - h * dy,  # y in -1..1
                z,  # z anywhere, but mostly between -1..1
                (u + dx * w) / tw,  # u of texture between 0..1
                1 - (v + dy * h) / th,  # v of texture between 0..1
            )
            for dx, dy in ((0, 0), (1, 0), (1, 1), (0, 1),)
        ]
        flat = [x for r in points for x in r]
        return flat
