import os

import moderngl

from src.locals.paths import SHADERS_DIR


def load_file(path: str):
    with open(path) as f:
        return f.read()


def load_shader(name: str, ctx: moderngl.Context):
    vertex_path = os.path.join(SHADERS_DIR, f"{name}_vertex.glsl")
    fragment_path = os.path.join(SHADERS_DIR, f"{name}_fragment.glsl")

    vertex = load_file(vertex_path)
    fragment = load_file(fragment_path)

    return ctx.program(vertex_shader=vertex, fragment_shader=fragment)
