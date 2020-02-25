# This file is generated by [gen_atlas.py]

import enum
from functools import lru_cache

TEX_WIDTH = 2048
TEX_HEIGHT = 2048

RECTS = [
    #   x,    y,    w,    h, offx, offy, orgw, orgh 
    (2   , 2   , 384 , 216 , 2   , 2   , 384 , 216 ),  # 0: BG_LAYER_0_SKY
    (390 , 2   , 384 , 216 , 2   , 2   , 384 , 216 ),  # 1: BG_LAYER_0_SKY_LIGHTENED
    (778 , 2   , 384 , 169 , 2   , 2   , 384 , 216 ),  # 2: BG_LAYER_1_CLOUDS
    (1942, 2   , 89  , 31  , 215 , 148 , 384 , 216 ),  # 3: BG_LAYER_2_CLOUND_LONELY
    (1166, 2   , 384 , 164 , 2   , 2   , 384 , 216 ),  # 4: BG_LAYER_3_MOUNTAINS
    (1554, 2   , 384 , 164 , 2   , 2   , 384 , 216 ),  # 5: BG_LAYER_3_MOUNTAINS_LIGHTENED
    (1166, 170 , 384 , 61  , 2   , 2   , 384 , 216 ),  # 6: BG_LAYER_4_DARK_LOW_CLOUDS
    (778 , 175 , 384 , 61  , 2   , 2   , 384 , 216 ),  # 7: BG_LAYER_5_LOW_CLOUDS
    (1554, 170 , 384 , 51  , 2   , 2   , 384 , 216 ),  # 8: BG_LAYER_6_LIGHT_CLOUDS
    (1554, 225 , 384 , 51  , 2   , 2   , 384 , 216 ),  # 9: BG_LAYER_6_LIGHT_CLOUDS_LIGHTENED
    (1942, 37  , 48  , 36  , 3   , 3   , 50  , 37  ),  # 10: ADVENTURER_AIR_ATTACK_3_END_00
    (1994, 37  , 46  , 30  , 5   , 3   , 50  , 37  ),  # 11: ADVENTURER_AIR_ATTACK_3_END_01
    (1942, 167 , 46  , 22  , 4   , 3   , 50  , 37  ),  # 12: ADVENTURER_AIR_ATTACK_3_END_02
    (1568, 368 , 18  , 26  , 17  , 4   , 50  , 37  ),  # 13: ADVENTURER_AIR_ATTACK1_00
    (1994, 71  , 46  , 30  , 4   , 5   , 50  , 37  ),  # 14: ADVENTURER_AIR_ATTACK1_01
    (1942, 193 , 29  , 30  , 8   , 6   , 50  , 37  ),  # 15: ADVENTURER_AIR_ATTACK1_02
    (1942, 227 , 27  , 31  , 7   , 6   , 50  , 37  ),  # 16: ADVENTURER_AIR_ATTACK1_03
    (1983, 132 , 34  , 31  , 17  , 4   , 50  , 37  ),  # 17: ADVENTURER_AIR_ATTACK2_00
    (2023, 132 , 23  , 31  , 18  , 5   , 50  , 37  ),  # 18: ADVENTURER_AIR_ATTACK2_01
    (1679, 337 , 16  , 26  , 17  , 6   , 50  , 37  ),  # 19: ADVENTURER_AIR_ATTACK2_02
    (1973, 242 , 27  , 30  , 10  , 6   , 50  , 37  ),  # 20: ADVENTURER_AIR_ATTACK3_LOOP_00
    (2007, 207 , 27  , 31  , 10  , 6   , 50  , 37  ),  # 21: ADVENTURER_AIR_ATTACK3_LOOP_01
    (1975, 207 , 28  , 31  , 10  , 7   , 50  , 37  ),  # 22: ADVENTURER_AIR_ATTACK3_RDY_00
    (1363, 266 , 27  , 22  , 9   , 3   , 50  , 37  ),  # 23: ADVENTURER_ATTACK1_00
    (1454, 337 , 25  , 20  , 10  , 3   , 50  , 37  ),  # 24: ADVENTURER_ATTACK1_01
    (1942, 77  , 34  , 36  , 17  , 3   , 50  , 37  ),  # 25: ADVENTURER_ATTACK1_02
    (1992, 167 , 27  , 36  , 17  , 3   , 50  , 37  ),  # 26: ADVENTURER_ATTACK1_03
    (1417, 235 , 19  , 32  , 17  , 3   , 50  , 37  ),  # 27: ADVENTURER_ATTACK1_04
    (1507, 359 , 18  , 26  , 17  , 3   , 50  , 37  ),  # 28: ADVENTURER_ATTACK2_00
    (1595, 311 , 18  , 27  , 17  , 3   , 50  , 37  ),  # 29: ADVENTURER_ATTACK2_01
    (1501, 235 , 20  , 27  , 15  , 3   , 50  , 37  ),  # 30: ADVENTURER_ATTACK2_02
    (1942, 132 , 37  , 29  , 12  , 3   , 50  , 37  ),  # 31: ADVENTURER_ATTACK2_03
    (1194, 259 , 32  , 21  , 4   , 3   , 50  , 37  ),  # 32: ADVENTURER_ATTACK2_04
    (1270, 235 , 31  , 22  , 4   , 3   , 50  , 37  ),  # 33: ADVENTURER_ATTACK2_05
    (1584, 280 , 20  , 26  , 21  , 3   , 50  , 37  ),  # 34: ADVENTURER_ATTACK3_00
    (1546, 299 , 20  , 26  , 22  , 3   , 50  , 37  ),  # 35: ADVENTURER_ATTACK3_01
    (1980, 105 , 48  , 23  , 4   , 3   , 50  , 37  ),  # 36: ADVENTURER_ATTACK3_02
    (1318, 267 , 31  , 19  , 5   , 3   , 50  , 37  ),  # 37: ADVENTURER_ATTACK3_03
    (1194, 235 , 34  , 20  , 2   , 3   , 50  , 37  ),  # 38: ADVENTURER_ATTACK3_04
    (1232, 235 , 34  , 20  , 2   , 3   , 50  , 37  ),  # 39: ADVENTURER_ATTACK3_05
    (1389, 300 , 21  , 26  , 17  , 3   , 50  , 37  ),  # 40: ADVENTURER_CAST_00
    (1786, 280 , 18  , 25  , 17  , 3   , 50  , 37  ),  # 41: ADVENTURER_CAST_01
    (1716, 334 , 17  , 25  , 18  , 3   , 50  , 37  ),  # 42: ADVENTURER_CAST_02
    (1230, 259 , 27  , 24  , 17  , 3   , 50  , 37  ),  # 43: ADVENTURER_CAST_03
    (1305, 235 , 27  , 24  , 17  , 3   , 50  , 37  ),  # 44: ADVENTURER_CAST_LOOP_00
    (2004, 274 , 29  , 24  , 15  , 3   , 50  , 37  ),  # 45: ADVENTURER_CAST_LOOP_01
    (1261, 261 , 27  , 24  , 17  , 3   , 50  , 37  ),  # 46: ADVENTURER_CAST_LOOP_02
    (1971, 276 , 29  , 24  , 15  , 3   , 50  , 37  ),  # 47: ADVENTURER_CAST_LOOP_03
    (1529, 385 , 16  , 29  , 23  , 4   , 50  , 37  ),  # 48: ADVENTURER_CRNR_CLMB_00
    (1671, 367 , 15  , 26  , 23  , 6   , 50  , 37  ),  # 49: ADVENTURER_CRNR_CLMB_01
    (1590, 370 , 15  , 24  , 22  , 7   , 50  , 37  ),  # 50: ADVENTURER_CRNR_CLMB_02
    (1808, 280 , 14  , 24  , 23  , 9   , 50  , 37  ),  # 51: ADVENTURER_CRNR_CLMB_03
    (1609, 394 , 15  , 24  , 23  , 9   , 50  , 37  ),  # 52: ADVENTURER_CRNR_CLMB_04
    (2032, 302 , 14  , 34  , 23  , 2   , 50  , 37  ),  # 53: ADVENTURER_CRNR_GRB_00
    (1654, 280 , 14  , 34  , 23  , 2   , 50  , 37  ),  # 54: ADVENTURER_CRNR_GRB_01
    (1414, 307 , 15  , 34  , 22  , 2   , 50  , 37  ),  # 55: ADVENTURER_CRNR_GRB_02
    (1631, 310 , 14  , 34  , 23  , 2   , 50  , 37  ),  # 56: ADVENTURER_CRNR_GRB_03
    (2023, 167 , 23  , 29  , 19  , 3   , 50  , 37  ),  # 57: ADVENTURER_CRNR_JMP_00
    (1292, 263 , 22  , 29  , 20  , 3   , 50  , 37  ),  # 58: ADVENTURER_CRNR_JMP_01
    (1648, 365 , 19  , 21  , 18  , 3   , 50  , 37  ),  # 59: ADVENTURER_CROUCH_00
    (1716, 308 , 20  , 22  , 17  , 3   , 50  , 37  ),  # 60: ADVENTURER_CROUCH_01
    (1649, 339 , 19  , 22  , 17  , 3   , 50  , 37  ),  # 61: ADVENTURER_CROUCH_02
    (1583, 398 , 17  , 21  , 19  , 3   , 50  , 37  ),  # 62: ADVENTURER_CROUCH_03
    (1570, 310 , 21  , 24  , 18  , 3   , 50  , 37  ),  # 63: ADVENTURER_DIE_00
    (1694, 280 , 19  , 24  , 19  , 3   , 50  , 37  ),  # 64: ADVENTURER_DIE_01
    (1717, 280 , 19  , 24  , 17  , 3   , 50  , 37  ),  # 65: ADVENTURER_DIE_02
    (1570, 342 , 22  , 22  , 18  , 3   , 50  , 37  ),  # 66: ADVENTURER_DIE_03
    (1826, 280 , 18  , 18  , 20  , 3   , 50  , 37  ),  # 67: ADVENTURER_DIE_04
    (1826, 302 , 15  , 17  , 23  , 3   , 50  , 37  ),  # 68: ADVENTURER_DIE_05
    (1848, 280 , 18  , 18  , 20  , 3   , 50  , 37  ),  # 69: ADVENTURER_DIE_06
    (1525, 266 , 17  , 31  , 20  , 7   , 50  , 37  ),  # 70: ADVENTURER_FALL_00
    (1463, 303 , 17  , 30  , 20  , 7   , 50  , 37  ),  # 71: ADVENTURER_FALL_01
    (1518, 331 , 21  , 24  , 18  , 3   , 50  , 37  ),  # 72: ADVENTURER_HURT_00
    (1740, 280 , 19  , 24  , 19  , 3   , 50  , 37  ),  # 73: ADVENTURER_HURT_01
    (1763, 280 , 19  , 24  , 17  , 3   , 50  , 37  ),  # 74: ADVENTURER_HURT_02
    (1366, 292 , 19  , 29  , 16  , 3   , 50  , 37  ),  # 75: ADVENTURER_IDLE_00
    (1433, 317 , 17  , 30  , 18  , 3   , 50  , 37  ),  # 76: ADVENTURER_IDLE_01
    (1394, 266 , 19  , 30  , 17  , 3   , 50  , 37  ),  # 77: ADVENTURER_IDLE_02
    (1318, 290 , 20  , 29  , 15  , 3   , 50  , 37  ),  # 78: ADVENTURER_IDLE_03
    (1363, 235 , 23  , 27  , 12  , 3   , 50  , 37  ),  # 79: ADVENTURER_IDLE_2_00
    (1390, 235 , 23  , 27  , 12  , 3   , 50  , 37  ),  # 80: ADVENTURER_IDLE_2_01
    (1942, 262 , 25  , 28  , 11  , 3   , 50  , 37  ),  # 81: ADVENTURER_IDLE_2_02
    (2004, 242 , 25  , 28  , 11  , 3   , 50  , 37  ),  # 82: ADVENTURER_IDLE_2_03
    (1764, 308 , 18  , 24  , 19  , 3   , 50  , 37  ),  # 83: ADVENTURER_ITEMS_00
    (1438, 288 , 21  , 25  , 18  , 3   , 50  , 37  ),  # 84: ADVENTURER_ITEMS_01
    (1631, 280 , 19  , 26  , 17  , 3   , 50  , 37  ),  # 85: ADVENTURER_ITEMS_02
    (1596, 342 , 20  , 24  , 17  , 3   , 50  , 37  ),  # 86: ADVENTURER_JUMP_00
    (1740, 308 , 20  , 22  , 17  , 3   , 50  , 37  ),  # 87: ADVENTURER_JUMP_01
    (1608, 280 , 19  , 27  , 19  , 5   , 50  , 37  ),  # 88: ADVENTURER_JUMP_02
    (1543, 358 , 21  , 23  , 16  , 11  , 50  , 37  ),  # 89: ADVENTURER_JUMP_03
    (1699, 337 , 13  , 30  , 21  , 5   , 50  , 37  ),  # 90: ADVENTURER_LADDER_CLIMB_00
    (2033, 242 , 13  , 27  , 21  , 7   , 50  , 37  ),  # 91: ADVENTURER_LADDER_CLIMB_01
    (1549, 385 , 13  , 30  , 21  , 5   , 50  , 37  ),  # 92: ADVENTURER_LADDER_CLIMB_02
    (1566, 398 , 13  , 27  , 21  , 7   , 50  , 37  ),  # 93: ADVENTURER_LADDER_CLIMB_03
    (1342, 292 , 20  , 28  , 19  , 3   , 50  , 37  ),  # 94: ADVENTURER_RUN_00
    (1525, 235 , 20  , 27  , 18  , 3   , 50  , 37  ),  # 95: ADVENTURER_RUN_01
    (1546, 329 , 20  , 25  , 18  , 3   , 50  , 37  ),  # 96: ADVENTURER_RUN_02
    (1336, 235 , 23  , 28  , 19  , 3   , 50  , 37  ),  # 97: ADVENTURER_RUN_03
    (1501, 266 , 20  , 27  , 18  , 3   , 50  , 37  ),  # 98: ADVENTURER_RUN_04
    (1483, 337 , 20  , 25  , 18  , 3   , 50  , 37  ),  # 99: ADVENTURER_RUN_05
    (1484, 297 , 34  , 15  , 7   , 3   , 50  , 37  ),  # 100: ADVENTURER_SLIDE_00
    (1546, 280 , 34  , 15  , 7   , 3   , 50  , 37  ),  # 101: ADVENTURER_SLIDE_01
    (1870, 280 , 15  , 21  , 20  , 11  , 50  , 37  ),  # 102: ADVENTURER_SMRSLT_00
    (1620, 348 , 24  , 17  , 16  , 12  , 50  , 37  ),  # 103: ADVENTURER_SMRSLT_01
    (1620, 369 , 18  , 21  , 22  , 8   , 50  , 37  ),  # 104: ADVENTURER_SMRSLT_02
    (1649, 318 , 26  , 17  , 13  , 9   , 50  , 37  ),  # 105: ADVENTURER_SMRSLT_03
    (1440, 235 , 34  , 16  , 7   , 3   , 50  , 37  ),  # 106: ADVENTURER_STAND_00
    (1484, 316 , 30  , 17  , 11  , 3   , 50  , 37  ),  # 107: ADVENTURER_STAND_01
    (1642, 390 , 22  , 17  , 17  , 3   , 50  , 37  ),  # 108: ADVENTURER_STAND_02
    (1694, 308 , 18  , 25  , 17  , 3   , 50  , 37  ),  # 109: ADVENTURER_SWRD_DRW_00
    (1672, 280 , 18  , 26  , 17  , 3   , 50  , 37  ),  # 110: ADVENTURER_SWRD_DRW_01
    (1478, 235 , 19  , 29  , 15  , 3   , 50  , 37  ),  # 111: ADVENTURER_SWRD_DRW_02
    (2004, 302 , 24  , 29  , 10  , 3   , 50  , 37  ),  # 112: ADVENTURER_SWRD_DRW_03
    (1166, 235 , 24  , 29  , 10  , 3   , 50  , 37  ),  # 113: ADVENTURER_SWRD_SHTE_00
    (1440, 255 , 19  , 29  , 15  , 3   , 50  , 37  ),  # 114: ADVENTURER_SWRD_SHTE_01
    (1522, 301 , 20  , 26  , 15  , 3   , 50  , 37  ),  # 115: ADVENTURER_SWRD_SHTE_02
    (1737, 334 , 17  , 25  , 18  , 3   , 50  , 37  ),  # 116: ADVENTURER_SWRD_SHTE_03
    (1463, 268 , 17  , 31  , 18  , 5   , 50  , 37  ),  # 117: ADVENTURER_WALL_SLIDE_00
    (1417, 271 , 17  , 32  , 18  , 5   , 50  , 37  ),  # 118: ADVENTURER_WALL_SLIDE_01
]
"""
Coordinates of the rectangles of each image in the atlas.
The coordinates increase left and up, as in a standard R²
coordinate system. 
Each tuple cooresponds to height numbers, in order:
    - the left coordinate of the sprite
    - the bottom coordinate
    - the with of the sprite
    - the height of the sprite
    - the x offset of the sprite in the original image
    - the y offset of the sprite in the original image
    - the width of the original image
    - the height of the original image
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
    ADVENTURER_AIR_ATTACK_3_END_00 = 10
    ADVENTURER_AIR_ATTACK_3_END_01 = 11
    ADVENTURER_AIR_ATTACK_3_END_02 = 12
    ADVENTURER_AIR_ATTACK1_00 = 13
    ADVENTURER_AIR_ATTACK1_01 = 14
    ADVENTURER_AIR_ATTACK1_02 = 15
    ADVENTURER_AIR_ATTACK1_03 = 16
    ADVENTURER_AIR_ATTACK2_00 = 17
    ADVENTURER_AIR_ATTACK2_01 = 18
    ADVENTURER_AIR_ATTACK2_02 = 19
    ADVENTURER_AIR_ATTACK3_LOOP_00 = 20
    ADVENTURER_AIR_ATTACK3_LOOP_01 = 21
    ADVENTURER_AIR_ATTACK3_RDY_00 = 22
    ADVENTURER_ATTACK1_00 = 23
    ADVENTURER_ATTACK1_01 = 24
    ADVENTURER_ATTACK1_02 = 25
    ADVENTURER_ATTACK1_03 = 26
    ADVENTURER_ATTACK1_04 = 27
    ADVENTURER_ATTACK2_00 = 28
    ADVENTURER_ATTACK2_01 = 29
    ADVENTURER_ATTACK2_02 = 30
    ADVENTURER_ATTACK2_03 = 31
    ADVENTURER_ATTACK2_04 = 32
    ADVENTURER_ATTACK2_05 = 33
    ADVENTURER_ATTACK3_00 = 34
    ADVENTURER_ATTACK3_01 = 35
    ADVENTURER_ATTACK3_02 = 36
    ADVENTURER_ATTACK3_03 = 37
    ADVENTURER_ATTACK3_04 = 38
    ADVENTURER_ATTACK3_05 = 39
    ADVENTURER_CAST_00 = 40
    ADVENTURER_CAST_01 = 41
    ADVENTURER_CAST_02 = 42
    ADVENTURER_CAST_03 = 43
    ADVENTURER_CAST_LOOP_00 = 44
    ADVENTURER_CAST_LOOP_01 = 45
    ADVENTURER_CAST_LOOP_02 = 46
    ADVENTURER_CAST_LOOP_03 = 47
    ADVENTURER_CRNR_CLMB_00 = 48
    ADVENTURER_CRNR_CLMB_01 = 49
    ADVENTURER_CRNR_CLMB_02 = 50
    ADVENTURER_CRNR_CLMB_03 = 51
    ADVENTURER_CRNR_CLMB_04 = 52
    ADVENTURER_CRNR_GRB_00 = 53
    ADVENTURER_CRNR_GRB_01 = 54
    ADVENTURER_CRNR_GRB_02 = 55
    ADVENTURER_CRNR_GRB_03 = 56
    ADVENTURER_CRNR_JMP_00 = 57
    ADVENTURER_CRNR_JMP_01 = 58
    ADVENTURER_CROUCH_00 = 59
    ADVENTURER_CROUCH_01 = 60
    ADVENTURER_CROUCH_02 = 61
    ADVENTURER_CROUCH_03 = 62
    ADVENTURER_DIE_00 = 63
    ADVENTURER_DIE_01 = 64
    ADVENTURER_DIE_02 = 65
    ADVENTURER_DIE_03 = 66
    ADVENTURER_DIE_04 = 67
    ADVENTURER_DIE_05 = 68
    ADVENTURER_DIE_06 = 69
    ADVENTURER_FALL_00 = 70
    ADVENTURER_FALL_01 = 71
    ADVENTURER_HURT_00 = 72
    ADVENTURER_HURT_01 = 73
    ADVENTURER_HURT_02 = 74
    ADVENTURER_IDLE_00 = 75
    ADVENTURER_IDLE_01 = 76
    ADVENTURER_IDLE_02 = 77
    ADVENTURER_IDLE_03 = 78
    ADVENTURER_IDLE_2_00 = 79
    ADVENTURER_IDLE_2_01 = 80
    ADVENTURER_IDLE_2_02 = 81
    ADVENTURER_IDLE_2_03 = 82
    ADVENTURER_ITEMS_00 = 83
    ADVENTURER_ITEMS_01 = 84
    ADVENTURER_ITEMS_02 = 85
    ADVENTURER_JUMP_00 = 86
    ADVENTURER_JUMP_01 = 87
    ADVENTURER_JUMP_02 = 88
    ADVENTURER_JUMP_03 = 89
    ADVENTURER_LADDER_CLIMB_00 = 90
    ADVENTURER_LADDER_CLIMB_01 = 91
    ADVENTURER_LADDER_CLIMB_02 = 92
    ADVENTURER_LADDER_CLIMB_03 = 93
    ADVENTURER_RUN_00 = 94
    ADVENTURER_RUN_01 = 95
    ADVENTURER_RUN_02 = 96
    ADVENTURER_RUN_03 = 97
    ADVENTURER_RUN_04 = 98
    ADVENTURER_RUN_05 = 99
    ADVENTURER_SLIDE_00 = 100
    ADVENTURER_SLIDE_01 = 101
    ADVENTURER_SMRSLT_00 = 102
    ADVENTURER_SMRSLT_01 = 103
    ADVENTURER_SMRSLT_02 = 104
    ADVENTURER_SMRSLT_03 = 105
    ADVENTURER_STAND_00 = 106
    ADVENTURER_STAND_01 = 107
    ADVENTURER_STAND_02 = 108
    ADVENTURER_SWRD_DRW_00 = 109
    ADVENTURER_SWRD_DRW_01 = 110
    ADVENTURER_SWRD_DRW_02 = 111
    ADVENTURER_SWRD_DRW_03 = 112
    ADVENTURER_SWRD_SHTE_00 = 113
    ADVENTURER_SWRD_SHTE_01 = 114
    ADVENTURER_SWRD_SHTE_02 = 115
    ADVENTURER_SWRD_SHTE_03 = 116
    ADVENTURER_WALL_SLIDE_00 = 117
    ADVENTURER_WALL_SLIDE_01 = 118
    
    
class Anim(enum.Enum):
    ADVENTURER_AIR_ATTACK_3_END = (10, 11, 12)
    ADVENTURER_AIR_ATTACK1 = (13, 14, 15, 16)
    ADVENTURER_AIR_ATTACK2 = (17, 18, 19)
    ADVENTURER_AIR_ATTACK3_LOOP = (20, 21)
    ADVENTURER_AIR_ATTACK3_RDY = (22,)
    ADVENTURER_ATTACK1 = (23, 24, 25, 26, 27)
    ADVENTURER_ATTACK2 = (28, 29, 30, 31, 32, 33)
    ADVENTURER_ATTACK3 = (34, 35, 36, 37, 38, 39)
    ADVENTURER_CAST = (40, 41, 42, 43)
    ADVENTURER_CAST_LOOP = (44, 45, 46, 47)
    ADVENTURER_CRNR_CLMB = (48, 49, 50, 51, 52)
    ADVENTURER_CRNR_GRB = (53, 54, 55, 56)
    ADVENTURER_CRNR_JMP = (57, 58)
    ADVENTURER_CROUCH = (59, 60, 61, 62)
    ADVENTURER_DIE = (63, 64, 65, 66, 67, 68, 69)
    ADVENTURER_FALL = (70, 71)
    ADVENTURER_HURT = (72, 73, 74)
    ADVENTURER_IDLE = (75, 76, 77, 78)
    ADVENTURER_IDLE_2 = (79, 80, 81, 82)
    ADVENTURER_ITEMS = (83, 84, 85)
    ADVENTURER_JUMP = (86, 87, 88, 89)
    ADVENTURER_LADDER_CLIMB = (90, 91, 92, 93)
    ADVENTURER_RUN = (94, 95, 96, 97, 98, 99)
    ADVENTURER_SLIDE = (100, 101)
    ADVENTURER_SMRSLT = (102, 103, 104, 105)
    ADVENTURER_STAND = (106, 107, 108)
    ADVENTURER_SWRD_DRW = (109, 110, 111, 112)
    ADVENTURER_SWRD_SHTE = (113, 114, 115, 116)
    ADVENTURER_WALL_SLIDE = (117, 118)
