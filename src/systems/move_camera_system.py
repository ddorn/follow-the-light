from math import cos, sin

import esper


class MoveCameraSystem(esper.Processor):
    def process(self, *args, **kwargs):
        time = kwargs["time"]
        camera = kwargs["camera"]
        w, h = camera.size
        speed = 1 / 3
        camera.center = (
            w / 2 + 100 * cos(time / speed),
            h / 2 + 100 * sin(time / speed),
        )
