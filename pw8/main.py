from input import input, loadThread
from output import saveZip
from domains import markManagement as mm
import curses

def main(stdscr):
    curses.curs_set(1)

    while True:
        stdscr.clear()
        title = "STUDENT MANAGEMENT SYSTEM"
        stdscr.addstr(10, 50, title, curses.A_BOLD | curses.A_REVERSE)
        stdscr.addstr(11, 50, "Choose a mode by enter the following number: ")
        stdscr.addstr(13, 50, "1. View all students", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(14, 50, "2. View all courses", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(15, 50, "3. View marks", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(16, 50, "4. Input new students", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(17, 50, "5. Input new courses", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(18, 50, "6. Input marks", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(19, 50, "7. Search for student", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(20, 50, "8. Search for course", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(21, 50, "0. EXIT", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.refresh()

        markManagement = mm.markManagement()
        backgroundThread = loadThread(markManagement, stdscr)
        backgroundThread.start()

        choice = stdscr.getkey()
        if choice == "0":
            saveZip(markManagement, stdscr)
            break
        elif choice in ["1", "2", "3", "4", "5", "6", "7", "8"]:
            input(stdscr, choice, markManagement)
            saveZip(markManagement, stdscr)
        else:
            stdscr.clear()
            stdscr.addstr(15, 50, "Error: You did not enter a valid key!")
            stdscr.refresh()
            stdscr.getch()

curses.wrapper(main)

"""
1. Task separation
2. Information (window) should be still available on the screen
3. More cases
"""