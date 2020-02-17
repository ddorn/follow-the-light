#!/usr/bin/env python3

import moderngl
import moderngl_window
import numpy as np

from src import shaders, shapes, atlas
from src.paths import ASSETS_DIR


class Window(moderngl_window.WindowConfig):
    gl_version = (3, 3)
    window_size = (800, 500)
    resource_dir = ASSETS_DIR
    title = "Follow the light"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        print("Follow the light !")

        self.prog = shaders.load_shader("simple", self.ctx)

        vertices, indices = shapes.get_rect(-1, -1, 2, 2)

        vbo = self.ctx.buffer(vertices.astype('f4').flatten().tobytes())
        ibo = self.ctx.buffer(indices.astype('i4').tobytes())

        atlas_path = "atlas.png"
        tex = self.load_texture_2d(atlas_path)
        self.sampler = self.ctx.sampler(filter=(moderngl.NEAREST, moderngl.NEAREST), texture=tex)
        tex.use()

        print(self.prog['rects'].value)
        self.prog['rects'].write(np.array(atlas.RECTS).astype('f4').tobytes())
        print(self.prog['rects'].value)

        self.vao = self.ctx.vertex_array(
            self.prog,
            [
                (vbo, "2f4 2f4 /v", "vert", "tex_coord"),
            ],
            ibo)

    def render(self, time: float, frame_time: float):
        self.prog['time'].value = time
        self.prog['sprite_id'].value = 6

        self.sampler.use()
        self.vao.render()


if __name__ == "__main__":
    moderngl_window.run_window_config(Window)
