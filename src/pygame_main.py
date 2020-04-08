import pygame
from pygame_input import Inputs, Axis, JoyAxis

from src import esper, logic, render
from src.data import atlas
from src.data.atlas import Anim, SpriteID
from src.logic.components import Pos, Player, Buffs, Vel, Collisions, Facing
from src.logic.state_machine import GroundedState, JumpState, FallState
from src.logic.state_machine.base import StateMachine
from src.render.components import Parallax, Animation, StateToAnimation, Camera, Sprite


class Window(render.BaseWindow):
    # window_size = (384, 216)

    def __init__(self, **kwargs):
        super().__init__()

        # Set up the world for all our entities
        self.world = esper.World()
        # High numbers are processed first
        self.world.add_processor(logic.LogicBundle(), 10)
        self.world.add_processor(render.RenderBundle(self), 0)

        self.camera = self.init_camera()
        self.inputs = self.init_inputs()
        self.init_background()
        self.init_player()

    def handle_events(self, events):
        super().handle_events(events)

        self.inputs.trigger(events)

    def init_background(self):
        layers = [
            SpriteID.BG_FOREST_0_SKY,
            SpriteID.BG_FOREST_1_SHADOWS,
            SpriteID.BG_FOREST_2_DARK_SHADOW,
            SpriteID.BG_FOREST_3_LIGHTS,
            SpriteID.BG_FOREST_4_TREES,
            SpriteID.BG_FOREST_5_BIGGER_TREES,
            SpriteID.BG_FOREST_5_MORE_TREES,
            SpriteID.BG_FOREST_6_LIGHTS,
            SpriteID.BG_FOREST_6_LEAVES,
            SpriteID.BG_FOREST_7_GRASS,
            SpriteID.BG_FOREST_8_DARK_GRASS,
        ]

        for i, sprite in enumerate(layers):
            for side in (True, False):
                height = atlas.RECTS[sprite.value][-1]
                self.world.create_entity(
                    Sprite(sprite),
                    Pos(0, height / 2, i / len(layers) - 1),
                    Parallax(side, -i * 0.05),
                )

    def init_camera(self):
        size = self.window_size
        return Camera((0, size[1] / 2), size)

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
            Pos(0, size[1] / 2, 0),
            Vel(0, 0, 0),
            Animation(Anim.ADVENTURER_ATTACK2, 0.1),
            StateMachine(GroundedState()),
            Buffs(),
            Collisions(),
            Facing(),
            StateToAnimation(
                {
                    GroundedState: Anim.ADVENTURER_RUN,
                    JumpState: Anim.ADVENTURER_JUMP,
                    FallState: Anim.ADVENTURER_FALL,
                }
            ),
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
