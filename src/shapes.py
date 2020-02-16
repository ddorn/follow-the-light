import numpy as np

def get_rect(x, y, w, h):
    vertices = np.array([
        (x, y),
        (x + w, y),
        (x + w, y + h),
        (x, y + h),
    ], dtype=float)

    indices = np.array([
        0, 1, 2, 0, 2, 3,
    ])

    return vertices, indices