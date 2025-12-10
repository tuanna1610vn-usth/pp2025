import curses

def output(init, stdscr):
    curses.curs_set(1)
    init.display(stdscr)
    init.rankings(stdscr)

    stdscr.clear()
    exit = "Thank you for using Student Management System!"
    stdscr.addstr(10, 15, exit, curses.A_BOLD)
    stdscr.addstr(12, 15, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()