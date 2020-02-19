import numpy as np


def get_rect(x, y, w, h, z=0):
    """
    Get a rectangle that lives in the z plane.

    Return an array of vec3+vec2 for 2d position and inner coordinates
    """
    pos = [
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 1),
        # (0.5, 0.5)
    ]
    vertices = np.array([(x + a * w, y + b * h, z, a, b) for a, b in pos], dtype=float)

    indices = np.array(
        [
            0,
            1,
            2,
            0,
            2,
            3,
            # 0, 1, 4,
            # 1, 2, 4,
            # 2, 3, 4,
            # 3, 0, 4,
        ]
    )

    return vertices, indices
