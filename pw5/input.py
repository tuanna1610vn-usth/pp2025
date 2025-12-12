from domains import mark_management as mm
from output import saveZip
import curses
import zipfile
import os

def input(stdscr, choice):
    curses.curs_set(1)
    init = mm.new()

    if os.path.exists("students.dat.zip"):
        try:
            with zipfile.ZipFile("students.dat.zip", "r") as zipf:
                zipf.extractall(".") # Compress and load data from zip file

            # Once the data is loaded successfully, load the extracted data
            init.loadFiles()

            
            stdscr.clear()
            stdscr.addstr(0, 0, "Data loaded successfully!", curses.A_BOLD)
            stdscr.addstr(1, 0, "Press any key to continue...")
            stdscr.refresh()
            stdscr.getch()
        except Exception as e:
            stdscr.clear()
            stdscr.addstr(f"Error loading data!: {str(e)}")
            stdscr.refresh()
            return

    if choice == "1":
        init.display(stdscr)
        init.rankings(stdscr)
        saveZip(init, stdscr)
    elif choice == "2":
        init.input(stdscr)
    return init