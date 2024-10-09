#!/usr/bin/python3
# -*- coding: utf-8 -*-

from random import shuffle
from math import *

from Anana import getch

def sqrt(x):
    return int(log(x)/log(2))

class Tournament:
    def __init__(self, contestants):
        self.side = ""
        self.contestants = contestants

    def vs(self, a, b):
        c = None
        print('   ===', self.side, self.phase, '===\n-',
                '1', a, '- 2', b)
        while c not in ['1', '2']:
            c = getch()
            if c == 'q':
                exit(0)

        print("\033[1A\033[K"*2, end="")

        w, l = {'1': (a, b), '2': (b, a)}[c]
        return w

    def do_round(self, inputs):
        """ return (winners_lst, loosers_lst) """
        nb = len(inputs)
        mp = sqrt(nb)
        llen = 2**(mp + 1)
        fr = inputs[llen-nb:]
        l = inputs[:llen-nb]

        inputs = fr or l

        w=list()
        for i in range(len(inputs)//2):
            if len(inputs)//2 == 1:
                self.phase = "Final"
            else:
                self.phase = str(i+1) + '/' + str(len(inputs)//2)
            w.append(self.vs(inputs[i], inputs[-i-1]))

        if fr:
            w = l + w
        return w, [x for x in inputs if x not in w]

    def do_tour(self, looser_side=True):
        shuffle(self.contestants)
        loosers = list()
        winners = self.contestants[:]
        while len(winners) > 1:
            if looser_side:
                while len(loosers) > max(1, len(winners)/2):
                    self.side = "Loosers Side :"
                    loosers, _ = self.do_round(loosers)

            self.side = "Winners Side :"
            winners, loosers2 = self.do_round(winners)
            loosers = loosers2 + loosers

        if looser_side:
            while len(loosers) > 1:
                self.side = "Loosers Side :"
                loosers, _ = self.do_round(loosers)
            self.side = "Grand Final :"
            ww = self.vs(winners[0], loosers[0])
        return ww

if __name__ == "__main__":
    import sys
    from pathlib import Path
    lst = list(map(str, range(8)))
    if len(sys.argv) > 1:
        p = Path(sys.argv[1])
        if p.exists():
            lst = p.read_text().splitlines()
    ww = Tournament(lst).do_tour()
    print(ww)

