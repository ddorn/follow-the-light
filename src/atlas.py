# This file is generated by [gen_atlas.py]

import enum

TEX_WIDTH = 2048
TEX_HEIGHT = 2048

RECTS = [
    #   x,     y,     w,     h
    2    , 2    , 384  , 216  ,  # 0
    390  , 2    , 384  , 216  ,  # 1
    778  , 2    , 384  , 216  ,  # 2
    1166 , 2    , 384  , 216  ,  # 3
    1554 , 2    , 384  , 216  ,  # 4
    2    , 222  , 384  , 216  ,  # 5
    390  , 222  , 384  , 216  ,  # 6
    778  , 222  , 384  , 216  ,  # 7
    1166 , 222  , 384  , 216  ,  # 8
    1554 , 222  , 384  , 216  ,  # 9
]
"""
Coordinates of the rectangles of each image in the atlas.
The coordinates increase left and up, as in a standard R² 
coordinate system. Indices corresponds to 4 time the sprite ids.
"""


class Sprite(enum.Enum):
    BG_LAYER_0_SKY = 0
    BG_LAYER_0_SKY_LIGHTENED = 1
    BG_LAYER_1_CLOUDS = 2
    BG_LAYER_2_CLOUND_LONELY = 3
    BG_LAYER_3_MOUNTAINS = 4
    BG_LAYER_3_MOUNTAINS_LIGHTENED = 5
    BG_LAYER_4_DARK_LOW_CLOUDS = 6
    BG_LAYER_5_LOW_CLOUDS = 7
    BG_LAYER_6_LIGHT_CLOUDS = 8
    BG_LAYER_6_LIGHT_CLOUDS_LIGHTENED = 9