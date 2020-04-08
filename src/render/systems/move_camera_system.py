from src import esper
from src.logic.components import Pos, Player
from src.render.components import Camera
from src.render.constants import CAMERA_BORDER_SIZE


class MoveCameraSystem(esper.Processor):
    def process(self, *args, camera: Camera, **kwargs):
        w, h = camera.size

        for e, (pos, _) in self.world.get_components(Pos, Player):
            if pos.x < camera.left + CAMERA_BORDER_SIZE:
                camera.left = pos.x - CAMERA_BORDER_SIZE
            elif pos.x > camera.right - CAMERA_BORDER_SIZE:
                camera.right = pos.x + CAMERA_BORDER_SIZE

            if pos.y < camera.bottom + CAMERA_BORDER_SIZE:
                camera.bottom = pos.y - CAMERA_BORDER_SIZE
            elif pos.y > camera.top - CAMERA_BORDER_SIZE:
                camera.top = pos.y + CAMERA_BORDER_SIZE

            break
