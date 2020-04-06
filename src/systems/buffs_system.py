from esper import Processor, World

from src.components import Buffs


class BuffSystem(Processor):
    """
    This system updates the time left for each buff in a Buffs component.
    """

    world: World

    def process(self, *args, frame_time, **kwargs):
        for e, buffs in self.world.get_component(Buffs):
            for key, value in buffs.items():
                buffs[key] = max(0.0, value - frame_time)

