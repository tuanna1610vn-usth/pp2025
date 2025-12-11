from input import input
from output import output
import curses

def main(stdscr):
    curses.curs_set(1)
    init = input(stdscr)
    output(init, stdscr)

curses.wrapper(main)