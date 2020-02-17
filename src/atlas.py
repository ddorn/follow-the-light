
# This file is generated by [gen_atlas.py]

import enum

RECTS = [
    # x,       y,         w,         h
    0.0,       0.0,       0.2,       0.5,       
    0.2,       0.0,       0.2,       0.5,       
    0.4,       0.0,       0.2,       0.5,       
    0.6,       0.0,       0.2,       0.5,       
    0.8,       0.0,       0.2,       0.5,       
    0.0,       0.5,       0.2,       0.5,       
    0.2,       0.5,       0.2,       0.5,       
    0.4,       0.5,       0.2,       0.5,       
    0.6,       0.5,       0.2,       0.5,       
    0.8,       0.5,       0.2,       0.5,       
]

class Sprite(enum.Enum):
    CLOUD_LONELY = 0,
    CLOUDS_BG = 1,
    CLOUDS_MG_1 = 2,
    CLOUDS_MG_1_LIGHTENED = 3,
    CLOUDS_MG_2 = 4,
    CLOUDS_MG_3 = 5,
    MOUNTAINS = 6,
    MOUNTAINS_LIGHTENED = 7,
    SKY = 8,
    SKY_LIGHTENED = 9

