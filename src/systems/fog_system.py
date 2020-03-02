import esper
import moderngl
import numpy as np

from src import shaders


class FogSystem(esper.Processor):
    world: esper.World

    def __init__(self, ctx: moderngl.Context):
        self.prog = shaders.load_shader("fog", ctx)

        # Set up the buffers
        vertices = np.array([
            (-1, -1),
            (-1, 1),
            (1, 1),
            (1, -1),
        ], dtype='f4')
        indices = np.array([0, 1, 2, 0, 2, 3], dtype='i4')
        self.vbo = ctx.buffer(vertices.tobytes())
        self.ibo = ctx.buffer(indices.tobytes())

        # The vao to draw actually things
        self.vao = ctx.vertex_array(
            self.prog, [(self.vbo, "2f4", "vert"), ], self.ibo,
        )

    def process(self, *args, **kwargs):
        if "u_time" in self.prog:
            self.prog["u_time"].value = kwargs["time"]
        if "u_resolution" in self.prog:
            self.prog["u_resolution"].value = kwargs["screen_size"]
        self.vao.render()
