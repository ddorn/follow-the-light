#!/usr/bin/env python3
import os
from random import random
from time import time

import pygame
import moderngl
import numpy as np
import moderngl_window
from src import shaders, shapes
from src.colors import random_color
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

        atlas_path = "background/ice/full.png"
        tex = self.load_texture_2d(atlas_path)
        self.sampler = self.ctx.sampler(filter=(moderngl.NEAREST, moderngl.NEAREST), texture=tex)
        tex.use()

        self.vao = self.ctx.simple_vertex_array(self.prog, vbo, 'vert', index_buffer=ibo)


    def render(self, time: float, frame_time: float):
        self.prog['time'].value = time
        self.sampler.use()
        self.vao.render()

if __name__ == "__main__":
    moderngl_window.run_window_config(Window)
