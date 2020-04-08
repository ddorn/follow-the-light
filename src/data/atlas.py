# This file is generated by [gen_atlas.py]

from typing import Tuple

TEX_WIDTH = 2048
TEX_HEIGHT = 2048

RECTS = [
    #   x,    y,    w,    h, offx, offy, orgw, orgh 
    (2   , 2   , 928 , 793 , 2   , 2   , 928 , 793 ),  # 0: BG_FOREST_0_SKY
    (934 , 2   , 928 , 414 , 2   , 2   , 928 , 793 ),  # 1: BG_FOREST_1_SHADOWS
    (934 , 701 , 928 , 271 , 2   , 66  , 928 , 793 ),  # 2: BG_FOREST_2_DARK_SHADOW
    (2   , 1574, 479 , 178 , 250 , 159 , 928 , 793 ),  # 3: BG_FOREST_3_LIGHTS
    (2   , 799 , 928 , 271 , 2   , 66  , 928 , 793 ),  # 4: BG_FOREST_4_TREES
    (934 , 976 , 928 , 271 , 2   , 66  , 928 , 793 ),  # 5: BG_FOREST_5_BIGGER_TREES
    (2   , 1074, 898 , 272 , 32  , 65  , 928 , 793 ),  # 6: BG_FOREST_5_MORE_TREES
    (934 , 420 , 928 , 277 , 2   , 323 , 928 , 793 ),  # 7: BG_FOREST_6_LEAVES
    (2   , 1350, 603 , 220 , 15  , 117 , 928 , 793 ),  # 8: BG_FOREST_6_LIGHTS
    (2   , 1976, 928 , 70  , 2   , 2   , 928 , 793 ),  # 9: BG_FOREST_7_GRASS
    (485 , 1574, 928 , 77  , 2   , 2   , 928 , 793 ),  # 10: BG_FOREST_8_DARK_GRASS
    (2   , 1756, 384 , 216 , 2   , 2   , 384 , 216 ),  # 11: BG_LAYER_0_SKY
    (390 , 1756, 384 , 216 , 2   , 2   , 384 , 216 ),  # 12: BG_LAYER_0_SKY_LIGHTENED
    (609 , 1350, 384 , 169 , 2   , 2   , 384 , 216 ),  # 13: BG_LAYER_1_CLOUDS
    (1166, 1775, 89  , 31  , 215 , 148 , 384 , 216 ),  # 14: BG_LAYER_2_CLOUND_LONELY
    (778 , 1655, 384 , 164 , 2   , 2   , 384 , 216 ),  # 15: BG_LAYER_3_MOUNTAINS
    (934 , 1823, 384 , 164 , 2   , 2   , 384 , 216 ),  # 16: BG_LAYER_3_MOUNTAINS_LIGHTENED
    (904 , 1251, 384 , 61  , 2   , 2   , 384 , 216 ),  # 17: BG_LAYER_4_DARK_LOW_CLOUDS
    (1166, 1655, 384 , 61  , 2   , 2   , 384 , 216 ),  # 18: BG_LAYER_5_LOW_CLOUDS
    (934 , 1991, 384 , 51  , 2   , 2   , 384 , 216 ),  # 19: BG_LAYER_6_LIGHT_CLOUDS
    (1166, 1720, 384 , 51  , 2   , 2   , 384 , 216 ),  # 20: BG_LAYER_6_LIGHT_CLOUDS_LIGHTENED
    (1259, 1775, 48  , 36  , 3   , 3   , 50  , 37  ),  # 21: ADVENTURER_AIR_ATTACK_3_END_00
    (904 , 1316, 46  , 30  , 5   , 3   , 50  , 37  ),  # 22: ADVENTURER_AIR_ATTACK_3_END_01
    (740 , 1523, 46  , 22  , 4   , 3   , 50  , 37  ),  # 23: ADVENTURER_AIR_ATTACK_3_END_02
    (845 , 1913, 18  , 26  , 17  , 4   , 50  , 37  ),  # 24: ADVENTURER_AIR_ATTACK1_00
    (954 , 1316, 46  , 30  , 4   , 5   , 50  , 37  ),  # 25: ADVENTURER_AIR_ATTACK1_01
    (821 , 1523, 29  , 30  , 8   , 6   , 50  , 37  ),  # 26: ADVENTURER_AIR_ATTACK1_02
    (886 , 1523, 27  , 31  , 7   , 6   , 50  , 37  ),  # 27: ADVENTURER_AIR_ATTACK1_03
    (702 , 1523, 34  , 31  , 17  , 4   , 50  , 37  ),  # 28: ADVENTURER_AIR_ATTACK2_00
    (904 , 1074, 23  , 31  , 18  , 5   , 50  , 37  ),  # 29: ADVENTURER_AIR_ATTACK2_01
    (997 , 1483, 16  , 26  , 17  , 6   , 50  , 37  ),  # 30: ADVENTURER_AIR_ATTACK2_02
    (948 , 1523, 27  , 30  , 10  , 6   , 50  , 37  ),  # 31: ADVENTURER_AIR_ATTACK3_LOOP_00
    (917 , 1523, 27  , 31  , 10  , 6   , 50  , 37  ),  # 32: ADVENTURER_AIR_ATTACK3_LOOP_01
    (854 , 1523, 28  , 31  , 10  , 7   , 50  , 37  ),  # 33: ADVENTURER_AIR_ATTACK3_RDY_00
    (608 , 1655, 27  , 22  , 9   , 3   , 50  , 37  ),  # 34: ADVENTURER_ATTACK1_00
    (827 , 1853, 25  , 20  , 10  , 3   , 50  , 37  ),  # 35: ADVENTURER_ATTACK1_01
    (1311, 1775, 34  , 36  , 17  , 3   , 50  , 37  ),  # 36: ADVENTURER_ATTACK1_02
    (790 , 1523, 27  , 36  , 17  , 3   , 50  , 37  ),  # 37: ADVENTURER_ATTACK1_03
    (601 , 1686, 19  , 32  , 17  , 3   , 50  , 37  ),  # 38: ADVENTURER_ATTACK1_04
    (820 , 1915, 18  , 26  , 17  , 3   , 50  , 37  ),  # 39: ADVENTURER_ATTACK2_00
    (778 , 1939, 18  , 27  , 17  , 3   , 50  , 37  ),  # 40: ADVENTURER_ATTACK2_01
    (718 , 1655, 20  , 27  , 15  , 3   , 50  , 37  ),  # 41: ADVENTURER_ATTACK2_02
    (661 , 1523, 37  , 29  , 12  , 3   , 50  , 37  ),  # 42: ADVENTURER_ATTACK2_03
    (518 , 1655, 32  , 21  , 4   , 3   , 50  , 37  ),  # 43: ADVENTURER_ATTACK2_04
    (485 , 1683, 31  , 22  , 4   , 3   , 50  , 37  ),  # 44: ADVENTURER_ATTACK2_05
    (816 , 1823, 20  , 26  , 21  , 3   , 50  , 37  ),  # 45: ADVENTURER_ATTACK3_00
    (778 , 1842, 20  , 26  , 22  , 3   , 50  , 37  ),  # 46: ADVENTURER_ATTACK3_01
    (609 , 1523, 48  , 23  , 4   , 3   , 50  , 37  ),  # 47: ADVENTURER_ATTACK3_02
    (979 , 1551, 31  , 19  , 5   , 3   , 50  , 37  ),  # 48: ADVENTURER_ATTACK3_03
    (609 , 1550, 34  , 20  , 2   , 3   , 50  , 37  ),  # 49: ADVENTURER_ATTACK3_04
    (740 , 1549, 34  , 20  , 2   , 3   , 50  , 37  ),  # 50: ADVENTURER_ATTACK3_05
    (693 , 1655, 21  , 26  , 17  , 3   , 50  , 37  ),  # 51: ADVENTURER_CAST_00
    (911 , 1908, 18  , 25  , 17  , 3   , 50  , 37  ),  # 52: ADVENTURER_CAST_01
    (997 , 1425, 17  , 25  , 18  , 3   , 50  , 37  ),  # 53: ADVENTURER_CAST_02
    (512 , 1709, 27  , 24  , 17  , 3   , 50  , 37  ),  # 54: ADVENTURER_CAST_03
    (520 , 1680, 27  , 24  , 17  , 3   , 50  , 37  ),  # 55: ADVENTURER_CAST_LOOP_00
    (979 , 1523, 29  , 24  , 15  , 3   , 50  , 37  ),  # 56: ADVENTURER_CAST_LOOP_01
    (543 , 1708, 27  , 24  , 17  , 3   , 50  , 37  ),  # 57: ADVENTURER_CAST_LOOP_02
    (485 , 1655, 29  , 24  , 15  , 3   , 50  , 37  ),  # 58: ADVENTURER_CAST_LOOP_03
    (800 , 1919, 16  , 29  , 23  , 4   , 50  , 37  ),  # 59: ADVENTURER_CRNR_CLMB_00
    (1035, 1504, 15  , 26  , 23  , 6   , 50  , 37  ),  # 60: ADVENTURER_CRNR_CLMB_01
    (1019, 1397, 15  , 24  , 22  , 7   , 50  , 37  ),  # 61: ADVENTURER_CRNR_CLMB_02
    (1038, 1373, 14  , 24  , 23  , 9   , 50  , 37  ),  # 62: ADVENTURER_CRNR_CLMB_03
    (1018, 1446, 15  , 24  , 23  , 9   , 50  , 37  ),  # 63: ADVENTURER_CRNR_CLMB_04
    (827 , 1877, 14  , 34  , 23  , 2   , 50  , 37  ),  # 64: ADVENTURER_CRNR_GRB_00
    (802 , 1881, 14  , 34  , 23  , 2   , 50  , 37  ),  # 65: ADVENTURER_CRNR_GRB_01
    (742 , 1690, 15  , 34  , 22  , 2   , 50  , 37  ),  # 66: ADVENTURER_CRNR_GRB_02
    (778 , 1901, 14  , 34  , 23  , 2   , 50  , 37  ),  # 67: ADVENTURER_CRNR_GRB_03
    (485 , 1709, 23  , 29  , 19  , 3   , 50  , 37  ),  # 68: ADVENTURER_CRNR_JMP_00
    (574 , 1687, 22  , 29  , 20  , 3   , 50  , 37  ),  # 69: ADVENTURER_CRNR_JMP_01
    (1014, 1539, 19  , 21  , 18  , 3   , 50  , 37  ),  # 70: ADVENTURER_CROUCH_00
    (1004, 1316, 20  , 22  , 17  , 3   , 50  , 37  ),  # 71: ADVENTURER_CROUCH_01
    (1012, 1513, 19  , 22  , 17  , 3   , 50  , 37  ),  # 72: ADVENTURER_CROUCH_02
    (1028, 1316, 17  , 21  , 19  , 3   , 50  , 37  ),  # 73: ADVENTURER_CROUCH_03
    (906 , 1854, 21  , 24  , 18  , 3   , 50  , 37  ),  # 74: ADVENTURER_DIE_00
    (842 , 1943, 19  , 24  , 19  , 3   , 50  , 37  ),  # 75: ADVENTURER_DIE_01
    (865 , 1943, 19  , 24  , 17  , 3   , 50  , 37  ),  # 76: ADVENTURER_DIE_02
    (903 , 1882, 22  , 22  , 18  , 3   , 50  , 37  ),  # 77: ADVENTURER_DIE_03
    (1038, 1401, 18  , 18  , 20  , 3   , 50  , 37  ),  # 78: ADVENTURER_DIE_04
    (551 , 1687, 15  , 17  , 23  , 3   , 50  , 37  ),  # 79: ADVENTURER_DIE_05
    (1044, 1423, 18  , 18  , 20  , 3   , 50  , 37  ),  # 80: ADVENTURER_DIE_06
    (742 , 1655, 17  , 31  , 20  , 7   , 50  , 37  ),  # 81: ADVENTURER_FALL_00
    (864 , 1823, 17  , 30  , 20  , 7   , 50  , 37  ),  # 82: ADVENTURER_FALL_01
    (802 , 1853, 21  , 24  , 18  , 3   , 50  , 37  ),  # 83: ADVENTURER_HURT_00
    (867 , 1915, 19  , 24  , 19  , 3   , 50  , 37  ),  # 84: ADVENTURER_HURT_01
    (888 , 1943, 19  , 24  , 17  , 3   , 50  , 37  ),  # 85: ADVENTURER_HURT_02
    (647 , 1675, 19  , 29  , 16  , 3   , 50  , 37  ),  # 86: ADVENTURER_IDLE_00
    (885 , 1823, 17  , 30  , 18  , 3   , 50  , 37  ),  # 87: ADVENTURER_IDLE_01
    (624 , 1681, 19  , 30  , 17  , 3   , 50  , 37  ),  # 88: ADVENTURER_IDLE_02
    (601 , 1722, 20  , 29  , 15  , 3   , 50  , 37  ),  # 89: ADVENTURER_IDLE_03
    (581 , 1655, 23  , 27  , 12  , 3   , 50  , 37  ),  # 90: ADVENTURER_IDLE_2_00
    (574 , 1720, 23  , 27  , 12  , 3   , 50  , 37  ),  # 91: ADVENTURER_IDLE_2_01
    (904 , 1109, 25  , 28  , 11  , 3   , 50  , 37  ),  # 92: ADVENTURER_IDLE_2_02
    (904 , 1141, 25  , 28  , 11  , 3   , 50  , 37  ),  # 93: ADVENTURER_IDLE_2_03
    (997 , 1397, 18  , 24  , 19  , 3   , 50  , 37  ),  # 94: ADVENTURER_ITEMS_00
    (717 , 1721, 21  , 25  , 18  , 3   , 50  , 37  ),  # 95: ADVENTURER_ITEMS_01
    (880 , 1857, 19  , 26  , 17  , 3   , 50  , 37  ),  # 96: ADVENTURER_ITEMS_02
    (870 , 1887, 20  , 24  , 17  , 3   , 50  , 37  ),  # 97: ADVENTURER_JUMP_00
    (997 , 1371, 20  , 22  , 17  , 3   , 50  , 37  ),  # 98: ADVENTURER_JUMP_01
    (906 , 1823, 19  , 27  , 19  , 5   , 50  , 37  ),  # 99: ADVENTURER_JUMP_02
    (845 , 1886, 21  , 23  , 16  , 11  , 50  , 37  ),  # 100: ADVENTURER_JUMP_03
    (894 , 1908, 13  , 30  , 21  , 5   , 50  , 37  ),  # 101: ADVENTURER_LADDER_CLIMB_00
    (1037, 1446, 13  , 27  , 21  , 7   , 50  , 37  ),  # 102: ADVENTURER_LADDER_CLIMB_01
    (761 , 1690, 13  , 30  , 21  , 5   , 50  , 37  ),  # 103: ADVENTURER_LADDER_CLIMB_02
    (1027, 1342, 13  , 27  , 21  , 7   , 50  , 37  ),  # 104: ADVENTURER_LADDER_CLIMB_03
    (625 , 1715, 20  , 28  , 19  , 3   , 50  , 37  ),  # 105: ADVENTURER_RUN_00
    (693 , 1685, 20  , 27  , 18  , 3   , 50  , 37  ),  # 106: ADVENTURER_RUN_01
    (778 , 1872, 20  , 25  , 18  , 3   , 50  , 37  ),  # 107: ADVENTURER_RUN_02
    (554 , 1655, 23  , 28  , 19  , 3   , 50  , 37  ),  # 108: ADVENTURER_RUN_03
    (693 , 1716, 20  , 27  , 18  , 3   , 50  , 37  ),  # 109: ADVENTURER_RUN_04
    (856 , 1857, 20  , 25  , 18  , 3   , 50  , 37  ),  # 110: ADVENTURER_RUN_05
    (512 , 1737, 34  , 15  , 7   , 3   , 50  , 37  ),  # 111: ADVENTURER_SLIDE_00
    (778 , 1823, 34  , 15  , 7   , 3   , 50  , 37  ),  # 112: ADVENTURER_SLIDE_01
    (1045, 1477, 15  , 21  , 20  , 11  , 50  , 37  ),  # 113: ADVENTURER_SMRSLT_00
    (1017, 1483, 24  , 17  , 16  , 12  , 50  , 37  ),  # 114: ADVENTURER_SMRSLT_01
    (1037, 1534, 18  , 21  , 22  , 8   , 50  , 37  ),  # 115: ADVENTURER_SMRSLT_02
    (997 , 1350, 26  , 17  , 13  , 9   , 50  , 37  ),  # 116: ADVENTURER_SMRSLT_03
    (639 , 1655, 34  , 16  , 7   , 3   , 50  , 37  ),  # 117: ADVENTURER_STAND_00
    (742 , 1728, 30  , 17  , 11  , 3   , 50  , 37  ),  # 118: ADVENTURER_STAND_01
    (1018, 1425, 22  , 17  , 17  , 3   , 50  , 37  ),  # 119: ADVENTURER_STAND_02
    (911 , 1937, 18  , 25  , 17  , 3   , 50  , 37  ),  # 120: ADVENTURER_SWRD_DRW_00
    (820 , 1945, 18  , 26  , 17  , 3   , 50  , 37  ),  # 121: ADVENTURER_SWRD_DRW_01
    (649 , 1708, 19  , 29  , 15  , 3   , 50  , 37  ),  # 122: ADVENTURER_SWRD_DRW_02
    (904 , 1173, 24  , 29  , 10  , 3   , 50  , 37  ),  # 123: ADVENTURER_SWRD_DRW_03
    (904 , 1206, 24  , 29  , 10  , 3   , 50  , 37  ),  # 124: ADVENTURER_SWRD_SHTE_00
    (670 , 1675, 19  , 29  , 15  , 3   , 50  , 37  ),  # 125: ADVENTURER_SWRD_SHTE_01
    (840 , 1823, 20  , 26  , 15  , 3   , 50  , 37  ),  # 126: ADVENTURER_SWRD_SHTE_02
    (997 , 1454, 17  , 25  , 18  , 3   , 50  , 37  ),  # 127: ADVENTURER_SWRD_SHTE_03
    (717 , 1686, 17  , 31  , 18  , 5   , 50  , 37  ),  # 128: ADVENTURER_WALL_SLIDE_00
    (672 , 1708, 17  , 32  , 18  , 5   , 50  , 37  ),  # 129: ADVENTURER_WALL_SLIDE_01
]
"""
Coordinates of the rectangles of each image in the atlas.
The coordinates increase left and up, as in a standard R²
coordinate system. 
Each tuple cooresponds to height numbers, in order:
    - the left coordinate of the sprite
    - the bottom coordinate
    - the width of the sprite
    - the height of the sprite
    - the x offset of the sprite in the original image
    - the y offset of the sprite in the original image
    - the width of the original image
    - the height of the original image
"""


class SpriteID:
    BG_FOREST_0_SKY = 0
    BG_FOREST_1_SHADOWS = 1
    BG_FOREST_2_DARK_SHADOW = 2
    BG_FOREST_3_LIGHTS = 3
    BG_FOREST_4_TREES = 4
    BG_FOREST_5_BIGGER_TREES = 5
    BG_FOREST_5_MORE_TREES = 6
    BG_FOREST_6_LEAVES = 7
    BG_FOREST_6_LIGHTS = 8
    BG_FOREST_7_GRASS = 9
    BG_FOREST_8_DARK_GRASS = 10
    BG_LAYER_0_SKY = 11
    BG_LAYER_0_SKY_LIGHTENED = 12
    BG_LAYER_1_CLOUDS = 13
    BG_LAYER_2_CLOUND_LONELY = 14
    BG_LAYER_3_MOUNTAINS = 15
    BG_LAYER_3_MOUNTAINS_LIGHTENED = 16
    BG_LAYER_4_DARK_LOW_CLOUDS = 17
    BG_LAYER_5_LOW_CLOUDS = 18
    BG_LAYER_6_LIGHT_CLOUDS = 19
    BG_LAYER_6_LIGHT_CLOUDS_LIGHTENED = 20
    ADVENTURER_AIR_ATTACK_3_END_00 = 21
    ADVENTURER_AIR_ATTACK_3_END_01 = 22
    ADVENTURER_AIR_ATTACK_3_END_02 = 23
    ADVENTURER_AIR_ATTACK1_00 = 24
    ADVENTURER_AIR_ATTACK1_01 = 25
    ADVENTURER_AIR_ATTACK1_02 = 26
    ADVENTURER_AIR_ATTACK1_03 = 27
    ADVENTURER_AIR_ATTACK2_00 = 28
    ADVENTURER_AIR_ATTACK2_01 = 29
    ADVENTURER_AIR_ATTACK2_02 = 30
    ADVENTURER_AIR_ATTACK3_LOOP_00 = 31
    ADVENTURER_AIR_ATTACK3_LOOP_01 = 32
    ADVENTURER_AIR_ATTACK3_RDY_00 = 33
    ADVENTURER_ATTACK1_00 = 34
    ADVENTURER_ATTACK1_01 = 35
    ADVENTURER_ATTACK1_02 = 36
    ADVENTURER_ATTACK1_03 = 37
    ADVENTURER_ATTACK1_04 = 38
    ADVENTURER_ATTACK2_00 = 39
    ADVENTURER_ATTACK2_01 = 40
    ADVENTURER_ATTACK2_02 = 41
    ADVENTURER_ATTACK2_03 = 42
    ADVENTURER_ATTACK2_04 = 43
    ADVENTURER_ATTACK2_05 = 44
    ADVENTURER_ATTACK3_00 = 45
    ADVENTURER_ATTACK3_01 = 46
    ADVENTURER_ATTACK3_02 = 47
    ADVENTURER_ATTACK3_03 = 48
    ADVENTURER_ATTACK3_04 = 49
    ADVENTURER_ATTACK3_05 = 50
    ADVENTURER_CAST_00 = 51
    ADVENTURER_CAST_01 = 52
    ADVENTURER_CAST_02 = 53
    ADVENTURER_CAST_03 = 54
    ADVENTURER_CAST_LOOP_00 = 55
    ADVENTURER_CAST_LOOP_01 = 56
    ADVENTURER_CAST_LOOP_02 = 57
    ADVENTURER_CAST_LOOP_03 = 58
    ADVENTURER_CRNR_CLMB_00 = 59
    ADVENTURER_CRNR_CLMB_01 = 60
    ADVENTURER_CRNR_CLMB_02 = 61
    ADVENTURER_CRNR_CLMB_03 = 62
    ADVENTURER_CRNR_CLMB_04 = 63
    ADVENTURER_CRNR_GRB_00 = 64
    ADVENTURER_CRNR_GRB_01 = 65
    ADVENTURER_CRNR_GRB_02 = 66
    ADVENTURER_CRNR_GRB_03 = 67
    ADVENTURER_CRNR_JMP_00 = 68
    ADVENTURER_CRNR_JMP_01 = 69
    ADVENTURER_CROUCH_00 = 70
    ADVENTURER_CROUCH_01 = 71
    ADVENTURER_CROUCH_02 = 72
    ADVENTURER_CROUCH_03 = 73
    ADVENTURER_DIE_00 = 74
    ADVENTURER_DIE_01 = 75
    ADVENTURER_DIE_02 = 76
    ADVENTURER_DIE_03 = 77
    ADVENTURER_DIE_04 = 78
    ADVENTURER_DIE_05 = 79
    ADVENTURER_DIE_06 = 80
    ADVENTURER_FALL_00 = 81
    ADVENTURER_FALL_01 = 82
    ADVENTURER_HURT_00 = 83
    ADVENTURER_HURT_01 = 84
    ADVENTURER_HURT_02 = 85
    ADVENTURER_IDLE_00 = 86
    ADVENTURER_IDLE_01 = 87
    ADVENTURER_IDLE_02 = 88
    ADVENTURER_IDLE_03 = 89
    ADVENTURER_IDLE_2_00 = 90
    ADVENTURER_IDLE_2_01 = 91
    ADVENTURER_IDLE_2_02 = 92
    ADVENTURER_IDLE_2_03 = 93
    ADVENTURER_ITEMS_00 = 94
    ADVENTURER_ITEMS_01 = 95
    ADVENTURER_ITEMS_02 = 96
    ADVENTURER_JUMP_00 = 97
    ADVENTURER_JUMP_01 = 98
    ADVENTURER_JUMP_02 = 99
    ADVENTURER_JUMP_03 = 100
    ADVENTURER_LADDER_CLIMB_00 = 101
    ADVENTURER_LADDER_CLIMB_01 = 102
    ADVENTURER_LADDER_CLIMB_02 = 103
    ADVENTURER_LADDER_CLIMB_03 = 104
    ADVENTURER_RUN_00 = 105
    ADVENTURER_RUN_01 = 106
    ADVENTURER_RUN_02 = 107
    ADVENTURER_RUN_03 = 108
    ADVENTURER_RUN_04 = 109
    ADVENTURER_RUN_05 = 110
    ADVENTURER_SLIDE_00 = 111
    ADVENTURER_SLIDE_01 = 112
    ADVENTURER_SMRSLT_00 = 113
    ADVENTURER_SMRSLT_01 = 114
    ADVENTURER_SMRSLT_02 = 115
    ADVENTURER_SMRSLT_03 = 116
    ADVENTURER_STAND_00 = 117
    ADVENTURER_STAND_01 = 118
    ADVENTURER_STAND_02 = 119
    ADVENTURER_SWRD_DRW_00 = 120
    ADVENTURER_SWRD_DRW_01 = 121
    ADVENTURER_SWRD_DRW_02 = 122
    ADVENTURER_SWRD_DRW_03 = 123
    ADVENTURER_SWRD_SHTE_00 = 124
    ADVENTURER_SWRD_SHTE_01 = 125
    ADVENTURER_SWRD_SHTE_02 = 126
    ADVENTURER_SWRD_SHTE_03 = 127
    ADVENTURER_WALL_SLIDE_00 = 128
    ADVENTURER_WALL_SLIDE_01 = 129
    
    
class Anim(Tuple[int]):
    ADVENTURER_AIR_ATTACK_3_END = (21, 22, 23)
    ADVENTURER_AIR_ATTACK1 = (24, 25, 26, 27)
    ADVENTURER_AIR_ATTACK2 = (28, 29, 30)
    ADVENTURER_AIR_ATTACK3_LOOP = (31, 32)
    ADVENTURER_AIR_ATTACK3_RDY = (33,)
    ADVENTURER_ATTACK1 = (34, 35, 36, 37, 38)
    ADVENTURER_ATTACK2 = (39, 40, 41, 42, 43, 44)
    ADVENTURER_ATTACK3 = (45, 46, 47, 48, 49, 50)
    ADVENTURER_CAST = (51, 52, 53, 54)
    ADVENTURER_CAST_LOOP = (55, 56, 57, 58)
    ADVENTURER_CRNR_CLMB = (59, 60, 61, 62, 63)
    ADVENTURER_CRNR_GRB = (64, 65, 66, 67)
    ADVENTURER_CRNR_JMP = (68, 69)
    ADVENTURER_CROUCH = (70, 71, 72, 73)
    ADVENTURER_DIE = (74, 75, 76, 77, 78, 79, 80)
    ADVENTURER_FALL = (81, 82)
    ADVENTURER_HURT = (83, 84, 85)
    ADVENTURER_IDLE = (86, 87, 88, 89)
    ADVENTURER_IDLE_2 = (90, 91, 92, 93)
    ADVENTURER_ITEMS = (94, 95, 96)
    ADVENTURER_JUMP = (97, 98, 99, 100)
    ADVENTURER_LADDER_CLIMB = (101, 102, 103, 104)
    ADVENTURER_RUN = (105, 106, 107, 108, 109, 110)
    ADVENTURER_SLIDE = (111, 112)
    ADVENTURER_SMRSLT = (113, 114, 115, 116)
    ADVENTURER_STAND = (117, 118, 119)
    ADVENTURER_SWRD_DRW = (120, 121, 122, 123)
    ADVENTURER_SWRD_SHTE = (124, 125, 126, 127)
    ADVENTURER_WALL_SLIDE = (128, 129)
