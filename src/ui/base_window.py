import os
from time import time

import moderngl
import pygame
from PIL import Image

from src.locals.paths import ASSETS_DIR


class BaseWindow:
    window_size = (650, 650 * 9 // 16)
    resource_dir = ASSETS_DIR
    title = "Follow the light"
    fps = 60

    def __init__(self):
        # Set up the window
        self.display = pygame.display.set_mode(self.window_size, pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
        pygame.display.set_caption(self.title)

        # Set up the ctx
        self.ctx = moderngl.create_context()
        self.ctx.enable(moderngl.BLEND)

        self.aspect_ratio = self.window_size[0] / self.window_size[1]
        """Desired width/height"""
        self.set_view_port()

        self.running = True
        self.start_time = time()

    def stop(self):
        self.running = False

    def render(self, *args):
        pass

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.stop()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                self.stop()
        elif event.type == pygame.VIDEORESIZE:
            self.resize(event.size)

    def resize(self, new_size):
        pygame.display.set_mode(new_size, pygame.OPENGL | pygame.DOUBLEBUF | pygame.RESIZABLE)
        self.window_size = new_size
        self.set_view_port()

    def load_texture_2d(self, path, flip=True):
        img: Image.Image = Image.open(os.path.join(self.resource_dir, path)).convert('RGBA')
        if flip:
            img = img.transpose(Image.FLIP_TOP_BOTTOM)
        tex = self.ctx.texture(img.size, 4, img.tobytes())
        return tex

    def run(self):
        clock = pygame.time.Clock()

        frames = 0
        while self.running:
            for event in pygame.event.get():
                self.handle_event(event)

            self.ctx.clear()
            self.render(time() - self.start_time, clock.get_time() / 1000.)

            pygame.display.flip()
            frames += 1
            clock.tick(self.fps)

        print("FPS:", frames / (time() - self.start_time))

    def set_view_port(self):
        expected_width = int(self.window_size[1] * self.aspect_ratio)
        expected_height = int(expected_width / self.aspect_ratio)

        if expected_width > self.window_size[0]:
            expected_width = self.window_size[0]
            expected_height = int(expected_width / self.aspect_ratio)

        blank_space_x = self.window_size[0] - expected_width
        blank_space_y = self.window_size[1] - expected_height

        self.ctx.viewport = (
            blank_space_x // 2,
            blank_space_y // 2,
            expected_width,
            expected_height
        )

