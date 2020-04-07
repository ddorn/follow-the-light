from pygame_input import Inputs

from src.components import Buffs, Player
from src.esper import Processor, World
from src.locals.constants import *


class InputSystem(Processor):
    """
    This system converts the inputs into buffs for entities.
    """

    world: World

    def process(self, *args, inputs: Inputs, **kwargs):
        for e, (player, buffs) in self.world.get_components(Player, Buffs):
            if inputs["vmove"].value > 0:
                buffs[WANT_JUMP] = INPUT_MAX_DELAY

            if inputs["hmove"].value < 0:
                buffs[WANT_LEFT] = INPUT_MAX_DELAY
            elif inputs["hmove"].value > 0:
                buffs[WANT_RIGHT] = INPUT_MAX_DELAY
