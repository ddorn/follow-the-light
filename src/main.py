#!/usr/bin/env python3
from random import random
from time import time

import pygame
import moderngl
import numpy as np

from src import shaders, shapes
from src.colors import random_color


def main():
    print("Follow the light !")

    pygame.init()

    display = pygame.display.set_mode((800, 500), pygame.OPENGL)
    ctx = moderngl.create_context()
    prog = shaders.load_shader("simple", ctx)

    vertices, indices = shapes.get_rect(-1, -1, 2, 2)
    colors = np.array([c for _ in vertices for c in random_color()])

    colors = colors.reshape((4, 3))
    print(vertices, colors)
    vertices = np.append(vertices, colors, axis=1)

    vbo = ctx.buffer(vertices.astype('f4').flatten().tobytes())
    ibo = ctx.buffer(indices.astype('i4').tobytes())

    vao = ctx.simple_vertex_array(prog, vbo, 'vert', 'v_color', index_buffer=ibo)

    print(ctx, ctx.screen, vbo, vao)

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        ctx.clear(1.0, 1.0, 1.0)
        vao.render()
        ctx.finish()
        pygame.display.flip()

        clock.tick(10000)
        print('\r', clock.get_fps(), end='', flush=True)


if __name__ == "__main__":
    main()
