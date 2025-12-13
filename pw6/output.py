import curses
import os
import zipfile

def output(init, stdscr):
    curses.curs_set(1)
    init.display(stdscr)
    init.rankings(stdscr)

    stdscr.clear()
    exit = "Thank you for using Student Management System!"
    stdscr.addstr(10, 15, exit, curses.A_BOLD)
    stdscr.addstr(12, 15, "Press any key to save and compress data...")
    stdscr.refresh()
    stdscr.getch()

    saveZip(init, stdscr)

def saveZip(init, stdscr):
    try:
        # Write data to text file first
        init.saveFiles()

        # After text file is saved, zip the file
        with zipfile.ZipFile("students.dat.zip", "w", zipfile.ZIP_DEFLATED) as zipf:
            if os.path.exists("students.bin"):
                zipf.write("students.bin")
                os.remove("students.bin")
            if os.path.exists("courses.bin"):
                zipf.write("courses.bin")
                os.remove("courses.bin")
            if os.path.exists("marks.bin"):
                zipf.write("marks.bin")
                os.remove("marks.bin")

        stdscr.clear()
        stdscr.addstr(10, 15, "Data saved and compressed successfully!", curses.A_BOLD)
        stdscr.addstr(12, 15, "Press any key to exit....")
        stdscr.refresh()
        stdscr.getch()
    except Exception as e:
        stdscr.clear()
        stdscr.addstr(5, 5, f"Error saving and compressing data: {str(e)}")
        stdscr.refresh()
        return