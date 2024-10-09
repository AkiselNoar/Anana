#!/usr/bin/python3
# -*- coding: utf-8 -*-

from itertools import *

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY = (65, 65, 65)
GREY = (130, 130, 130)
LIGHT_GREY = (195, 195, 195)

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
PURPLE = (255, 255, 0)

def int2color(c):
    c = c%(256**3)
    b, c = c%256, c//256
    g, r = c%256, c//256
    return (r, g, b)

def hex2rgb(value):
    value = value.lstrip('#')
    lv = len(value)
    return tuple(int(value[i:i + lv // 3], 16) for i in range(0, lv, lv // 3))

def cycle_colors(start=0, end=256, step=1):
    for c in cycle(product(range(start, end, step), range(start, end, step), range(start, end, step))):
        yield c
