from domains import mark_management as mm
import curses

def input(stdscr):
    curses.curs_set(1)
    init = mm.new()
    init.input(stdscr)
    return init