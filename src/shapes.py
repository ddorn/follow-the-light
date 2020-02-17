import numpy as np

def get_rect(x, y, w, h):
    vertices = np.array([
        (x, y),
        (x + w, y),
        (x + w, y + h),
        (x, y + h),
        (x + w / 2, y + h / 2),
    ], dtype=float)

    indices = np.array([
        # 0, 1, 2, 0, 2, 3,
        0, 1, 4,
        1, 2, 4,
        2, 3, 4,
        3, 0, 4,
    ])

    return vertices, indices