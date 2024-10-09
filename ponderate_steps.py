#!/usr/bin/python3
# -*- coding: utf-8 -*-

from pathlib import Path
from random import choices, choice

def get_step_num(p):
    return int(p.name.split('_')[-1].lstrip('0') or 0)

def get_dv(o):

    res = dict()
    dis = dict()
    for p in Path(o).glob("Step_*"):
        l = len(list(p.glob("*")))
        ratio = (10+2*get_step_num(p))
        res[p] = ratio
        dis[ratio] = p, f"{l:<7} {ratio:<5}", res[p]

    for k, v in sorted(dis.items(), key= lambda x: x[0]):
        break
        print(*v)

    return res

def f_exclude(x, excludes):
    r = x in excludes or x in list(map(lambda n: Path(n).stem.split('_')[0], excludes))
    return r

def ch(dv, exclude=[]):
    l = []
    while not l:
        p = choices(list(dv.keys()), list(dv.values()))[0]
        l = list(filter(lambda x: x not in exclude, p.glob('*')))
        #l = list(filter(lambda x: f_exclude(x, exclude), p.glob('*')))
        if not l:
            del dv[p]
    c = choice(l)
    return c

def main():
    pass

if __name__ == "__main__":
    main()

