import struct

import esper
import moderngl
import moderngl_window
import numpy as np

from src import shaders, atlas
from src.atlas import Sprite
from src.components import Pos


BUFFER_SIZE = 100


class DrawSpriteSystem(esper.Processor):
    world: esper.World

    def __init__(
        self, ctx: moderngl.Context, window_conf: moderngl_window.WindowConfig
    ):
        self.prog = shaders.load_shader("texture", ctx)
        self.prog["tex_size"].value = (atlas.TEX_WIDTH, atlas.TEX_HEIGHT)

        # Load the texture with nearest filter
        atlas_path = "atlas.png"
        tex = window_conf.load_texture_2d(atlas_path, flip=True)
        # tex.filter = (moderngl.NEAREST, moderngl.NEAREST)
        tex.use()

        # Set up the buffers
        self.vbo = ctx.buffer(reserve=BUFFER_SIZE * 20 * 4)
        self.ibo = ctx.buffer(reserve=BUFFER_SIZE * 6 * 4)

        # The vao to draw actually things
        self.vao = ctx.vertex_array(
            self.prog, [(self.vbo, "3f4 2f4 /v", "vert", "tex_coord"),], self.ibo,
        )

    def process(self, *args, **kwargs):
        self.vbo.clear()
        self.ibo.clear()
        self.prog["camera"].value = kwargs["camera"].as_vec4()
        if "screen_size" in self.prog:
            self.prog["screen_size"].value = kwargs["screen_size"]
        if "u_time" in self.prog:
            self.prog["u_time"].value = kwargs["time"]

        tex_size = atlas.TEX_WIDTH, atlas.TEX_HEIGHT
        indices = np.array([0, 1, 2, 0, 2, 3], dtype="i4")

        qte = 0
        for e, (sprite, pos) in self.world.get_components(Sprite, Pos):
            assert (
                qte + 1 < BUFFER_SIZE
            ), "You have a lot of sprites now, good job ! You need bigger buffer though"

            # We compute the xyz coordinates of each point and the uv coordinate
            # in the texture
            points = self.points(pos, atlas.RECTS[sprite.value], tex_size)

            bytes = struct.pack("20f", *points)
            self.vbo.write(bytes, offset=qte * len(bytes))

            # The  indices are about the next four points we just wrote
            bytes = indices.tobytes()
            self.ibo.write(bytes, offset=qte * len(bytes))
            indices += 4

            qte += 1

        self.vao.render()

    def points(self, xyz, sprite, tex_size):
        x, y, z = xyz
        u, v, w, h, dx, dy, _, _ = sprite
        tw, th = tex_size

        x += dx
        y += dy

        points = [
            (
                x + w * dx,  # x in screen coordinates
                y + h * dy,  # y in screen coordinates
                z,  # z anywhere, but mostly between -1..1
                (u + dx * w) / tw,  # u of texture between 0..1
                (v + dy * h) / th,  # v of texture between 0..1
            )
            for dx, dy in ((0, 0), (1, 0), (1, 1), (0, 1),)
        ]
        flat = [x for r in points for x in r]
        return flat
