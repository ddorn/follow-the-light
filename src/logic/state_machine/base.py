from typing import Optional

from esper import World


class StateMachine:
    def __init__(self, initial: "State"):
        self.state = initial


class State:
    def next_state(self, entity: int, world: World) -> Optional["State"]:
        """
        Return the next state if this on is over.

        :param entity: the entity which has this state
        :param world: the world in which the entity is
        :return: The next state of the entity
        """

        raise NotImplementedError

    def update(self, entity: int, world: World):
        """
        Update the entity that have this state.

        When this method is always called when the state is valid,
        ie, the player is indeed jumping, provided that `next_state`
        was implemented correctly for the other states.

        :param entity: the entity which has this state
        :param world: the world in which the entity is
        """

        raise NotImplementedError

    def __str__(self):
        return f"{self.__class__.__name__}()"
