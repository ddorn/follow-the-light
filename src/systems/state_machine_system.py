import esper

from src.systems.state_machine.base import StateMachine


class StateMachineSystem(esper.Processor):
    world: esper.World

    def process(self, *args, **kwargs):

        for e, state_machine in self.world.get_component(StateMachine):
            state = state_machine.state.next_state(e, self.world)
            if state is not None:
                # Potentially we could add state.enter() and state.exit()
                # methods if they are needed.
                self.state = state
            state_machine.state.update(e, self.world)
