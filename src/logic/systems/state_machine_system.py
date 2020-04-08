from src import esper
from src.logic.state_machine.base import StateMachine


class StateMachineSystem(esper.Processor):
    def process(self, *args, **kwargs):

        for e, sm in self.world.get_component(StateMachine):
            state = sm.state.next_state(e, self.world)
            if state is not None:
                # Potentially we could add state.enter() and state.exit()
                # methods if they are needed.
                sm.state = state
            sm.state.update(e, self.world)
