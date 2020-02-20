# This file is generated by [gen_atlas.py]

import enum

TEX_WIDTH = 2048
TEX_HEIGHT = 2048
RECTS = [
    #   x,     y,     w,     h
    2    , 2    , 384  , 216  ,
    390  , 2    , 384  , 216  ,
    778  , 2    , 384  , 216  ,
    1166 , 2    , 384  , 216  ,
    1554 , 2    , 384  , 216  ,
    2    , 222  , 384  , 216  ,
    390  , 222  , 384  , 216  ,
    778  , 222  , 384  , 216  ,
    1166 , 222  , 384  , 216  ,
    1554 , 222  , 384  , 216  ,
]


class Sprite(enum.Enum):
    BG_LAYER_0_SKY_LIGHTENED = 0
    BG_LAYER_0_SKY = 1
    BG_LAYER_1_CLOUDS = 2
    BG_LAYER_2_CLOUND_LONELY = 3
    BG_LAYER_3_MOUNTAINS_LIGHTENED = 4
    BG_LAYER_3_MOUNTAINS = 5
    BG_LAYER_4_DARK_LOW_CLOUDS = 6
    BG_LAYER_5_LOW_CLOUDS = 7
    BG_LAYER_6_LIGHT_CLOUDS_LIGHTENED = 8
    BG_LAYER_6_LIGHT_CLOUDS = 9