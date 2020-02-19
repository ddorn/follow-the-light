from dataclasses import dataclass


@dataclass
class Camera:
    """
    The game's 2D camera. The coordinate system has the same axis
    as the usual R² plane - ie. increase right and up.

    Actual conversion between screen coords and opengl view is in
    the vertex shader.
    """

    center: (float, float)
    size: (float, float)

    def as_vec4(self):
        return self.center + self.size

    @property
    def left(self):
        return self.center[0] - self.size[0] / 2
