#!/usr/bin/python3
# -*- coding: utf-8 -*-

def set_cursor(x, y):
    """ Position the bash cursor """
    print(f"\033[{x};{y}H]", end="")

def cursor_up(n=1):
    """ Move the bash cursor n line up """
    print(f"\033[{n}A", end="")

def cursor_down(n=1):
    """ Move the bash cursor n line down """
    print(f"\033[{n}B", end="")

def cursor_fwd(n=1):
    """ Move the bash cursor n column forward """
    print(f"\033[{n}C", end="")

def cursor_bwd(n=1):
    """ Move the bash cursor n column backward """
    print(f"\033[{n}N", end="")

def clear_console():
    """ Clear bash console, move to (0, 0) """
    print(f"\033[2J", end="")

def clear_line():
    """ Clear to the end of the bash line """
    print(f"\033[K", end="")

def save_pos():
    """ Save bash cursor position """
    print(f"\033[s", end="")

def load_pos():
    """ Load bash cursor position """
    print(f"\033[u", end="")
