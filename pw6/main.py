from input import input
from output import output
import curses

def main(stdscr):
    curses.curs_set(1)

    while True:
        stdscr.clear()
        title = "STUDENT MANAGEMENT SYSTEM"
        stdscr.addstr(10, 20, title, curses.A_BOLD | curses.A_REVERSE)
        stdscr.addstr(11, 20, "Choose a mode by enter the following number: ")
        stdscr.addstr(13, 20, "1. View all students, courses information and marks", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(14, 20, "2. Input new students, courses information and marks", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(15, 20, "0. EXIT", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.refresh()

        choice = stdscr.getkey()
        if choice == "0":
            break
        elif choice == "1" or choice == "2":
            init = input(stdscr, choice)
            if choice == "2":
                output(init, stdscr)
        else:
            stdscr.clear()
            stdscr.addstr(10, 20, "Error: You did not enter a valid key!")
            stdscr.refresh()
            stdscr.getch()

curses.wrapper(main)