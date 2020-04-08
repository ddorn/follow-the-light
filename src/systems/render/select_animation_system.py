
from src.components import Animation, StateToAnimation
from src.esper import Processor
from src.systems.state_machine.base import StateMachine


class SelectAnimationSystem(Processor):
    def process(self, *args, **kwargs):
        anim: Animation
        sm: StateMachine
        state2anim: StateToAnimation
        for e, (sm, anim, state2anim) in self.world.get_components(StateMachine, Animation, StateToAnimation):
            a = state2anim.state_to_animation[sm.state.__class__]
            if anim.anim == a:
                pass
            else:
                anim.replace(a)
