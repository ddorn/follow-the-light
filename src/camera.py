from dataclasses import dataclass


@dataclass
class Camera:
    center: (float, float)
    size: (float, float)

    def as_vec4(self):
        return self.center + self.size
