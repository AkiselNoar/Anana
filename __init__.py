"""
My utils
"""

import os, sys
import termios, tty
import hashlib
from math import *
import shutil
from pathlib import Path
from . import Consts

def getch():
    """
    Wait for a single character input and return it
    raise KeyboardIterrupt
    block sending to background events
    """
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
        if ord(ch) == 3:
            raise KeyboardInterrupt
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

def md5(fname):
    """
    Return md5sum of a file
    """
    hash_md5 = hashlib.md5()
    with open(fname, 'rb') as f:
        for c in iter(lambda: f.read(4096), b""):
            hash_md5.update(c)
    return hash_md5.hexdigest()

def safe_move(orig, dest_path, copy=False):
    """
    Move orig file to dest_path directory
    File will be renamed with "_<nb>" whit nb incrementing
    until dest file doesn't already exists or dest file has the same md5sum
    If Copy = True, file won't be erased after copy
    """
    assert os.path.isfile(orig), f"first argument ({orig}) must be a file"
    assert os.path.isdir(dest_path), f"second argument ({dest_path}) must be a directory"
    fn = ofn = os.path.basename(orig)
    dest = os.path.join(dest_path, fn)
    ext = ""
    ffn = fn
    if '.' in fn:
        ext = '.' + fn.split('.')[-1]
        ffn = '.'.join(fn.split('.')[:-1])
    i = 0
    md5o = md5(orig)
    while os.path.exists(dest) and md5(dest) != md5o:
        i += 1
        fn = f"{ffn}_{i}{ext}"
        dest = os.path.join(dest_path, fn)
    if copy:
        shutil.copyfile(orig, dest)
    else:
        shutil.move(orig, dest)
    return dest

def going_round(nb_pts, center, radius, offset=0, clockwise=True):
    """ Generator of points equaly distributed in a circle
    Radius can be send a each iteration
    nb_pts : integer number of points which will be yielded
    center : tuple of 2 integers center of the circle
    radius : distance between the points and the center
    offset : angle offset of the first point
        0 : first point east
        pi/2 : first point north
        pi : first point west
        3*pi/2 : first point south
    """
    for i in range(nb_pts):
        i *= [-1, 1][clockwise]
        r = (int(radius * cos(i*2*pi/nb_pts+offset) + center[0]),
                int(radius * sin(i*2*pi/nb_pts+offset) + center[1]))
        nradius = (yield r)
        radius = radius if nradius is None else nradius

def _old_going_round(nb_pts, center, radius, offset=0, clockwise=True):
    """ Generator of points equaly distributed in a circle
    nb_pts : integer number of points which will be yielded
    center : tuple of 2 integers center of the circle
    radius : distance between the points and the center
    offset : angle offset of the first point
        0 : first point east
        pi/2 : first point north
        pi : first point west
        3*pi/2 : first point south
    """
    for i in range(nb_pts):
        i *= [-1, 1][clockwise]
        yield (int(radius * cos(i*2*pi/nb_pts+offset) + center[0]),
                int(radius * sin(i*2*pi/nb_pts+offset) + center[1]))

def going_round_nround(*args, **kwargs):
    """ going_round forever """
    while 1:
        yield from going_round(*args, **kwargs)

def pts_in_poly(pos, poly):
    """ return True if pos in poly
    pos: tuple of 2 integers
    poly: list of tuples of 2 integers"""
    x, y = pos
    n = len(poly)
    inside = False
    xints = 0.0
    p1x, p1y = poly[0]
    for i in range(n+1):
        p2x, p2y = poly[i%n]
        if (y > min(p1y, p2y)
                and y <= max(p1y,p2y)
                and x <= max(p1x,p2x)):
            if p1y != p2y:
                xints = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
            if p1x == p2x or x <= xints:
                inside = not inside
        p1x,p1y = p2x,p2y
    return inside

def list_from_file(path):
    res = list()
    for l in Path(path).read_text().splitlines():
        res.extend(l.split('#')[0].split())
    return res
