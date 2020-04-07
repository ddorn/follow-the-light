from math import cos, sin

from src import esper


class MoveCameraSystem(esper.Processor):
    def process(self, *args, **kwargs):
        time = kwargs["time"]
        camera = kwargs["camera"]
        w, h = camera.size
        speed = 0
        camera.center = (
            w / 2 + 100 * cos(time * speed),
            h / 2 + 100 * sin(time * speed),
        )
