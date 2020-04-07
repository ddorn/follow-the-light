import esper
import pygame
from pygame_input import Inputs, Axis, JoyAxis

from src import systems
from src.graphism.atlas import Sprite, Anim
from src.camera import Camera
from src.components import Pos, Parallax, Player, Animation
from src.ui import BaseWindow


class Window(BaseWindow):
    # window_size = (384, 216)

    def __init__(self, **kwargs):
        super().__init__()

        # Set up the world for all our entities
        self.world = esper.World()
        # High numbers are processed first
        self.world.add_processor(systems.BuffSystem(), 6)
        self.world.add_processor(systems.StateMachineSystem(), 5)
        self.world.add_processor(systems.PlayerMoveSystem(), 4)
        self.world.add_processor(systems.MoveCameraSystem(), 3)
        self.world.add_processor(systems.ParallaxSystem(), 2)
        self.world.add_processor(systems.AnimationSystem(), 2)
        self.world.add_processor(systems.DrawSpriteSystem(self.ctx, self), 1)
        self.world.add_processor(systems.FogSystem(self.ctx), 0)
        self.init_background()
        self.camera = self.init_camera()
        self.inputs = self.init_inputs()
        self.init_player()

    def handle_events(self, events):
        super().handle_events(events)

        self.inputs.trigger(events)

    def init_background(self):
        layers = [
            Sprite.BG_FOREST_0_SKY,
            Sprite.BG_FOREST_1_SHADOWS,
            Sprite.BG_FOREST_2_DARK_SHADOW,
            Sprite.BG_FOREST_3_LIGHTS,
            Sprite.BG_FOREST_4_TREES,
            Sprite.BG_FOREST_5_BIGGER_TREES,
            Sprite.BG_FOREST_5_MORE_TREES,
            Sprite.BG_FOREST_6_LIGHTS,
            Sprite.BG_FOREST_6_LEAVES,
            Sprite.BG_FOREST_7_GRASS,
            Sprite.BG_FOREST_8_DARK_GRASS,
        ]

        for i, sprite in enumerate(layers):
            for side in (True, False):
                self.world.create_entity(
                    sprite, Pos(0, 0, i / len(layers) - 1), Parallax(side, -i * 5)
                )

        for i, sprite in enumerate(layers):
            for side in (True, False):
                self.world.create_entity(
                    sprite, Pos(0, 0, i / len(layers) - 1), Parallax(side, -i * 5)
                )

    def init_camera(self):
        size = self.window_size
        return Camera((size[0] / 2, size[1] / 2), size)

    def init_inputs(self):
        pygame.joystick.init()
        for i in range(pygame.joystick.get_count()):
            pygame.joystick.Joystick(i).init()

        inputs = Inputs()
        inputs["hmove"] = Axis(
            (pygame.K_LEFT, pygame.K_a), (pygame.K_RIGHT, pygame.K_d), JoyAxis(0)
        )
        inputs["vmove"] = Axis(
            (pygame.K_DOWN, pygame.K_s),
            (pygame.K_UP, pygame.K_w),
            JoyAxis(1, reversed=True),
        )

        return inputs

    def init_player(self):
        size = self.window_size
        self.world.create_entity(
            Player(),
            Pos(size[0] / 2, size[1] / 2, 0),
            Animation(Anim.ADVENTURER_ATTACK2, 5 / 60),
        )

    def render(self, time: float, frame_time: float):
        self.world.process(
            ctx=self.ctx,
            time=time,
            frame_time=frame_time,
            camera=self.camera,
            screen_size=self.window_size,  # TODO: should be real window size
            inputs=self.inputs,
        )


if __name__ == "__main__":
    Window().run()
