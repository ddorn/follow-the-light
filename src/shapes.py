import numpy as np

def get_rect(x, y, w, h):
    pos = [
        (0, 0),
        (1, 0),
        (1, 1),
        (0, 1),
        # (0.5, 0.5)
    ]
    vertices = np.array([
        (x + a*w, y + b * h, a, b)
        for a, b in pos
    ], dtype=float)

    indices = np.array([
        0, 1, 2, 0, 2, 3,
        # 0, 1, 4,
        # 1, 2, 4,
        # 2, 3, 4,
        # 3, 0, 4,
    ])

    return vertices, indices