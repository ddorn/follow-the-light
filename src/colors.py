from colorsys import hsv_to_rgb
from random import random


def random_color():
    return hsv_to_rgb(random(), 1, 1)