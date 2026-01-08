import threading
import curses
import zipfile
import os

def input(stdscr, choice, markManagement):
    curses.curs_set(1)
    if choice == "1":
        markManagement.displayAllStudents(stdscr)
        markManagement.rankings(stdscr)
    elif choice == "2":
        markManagement.displayAllCourses(stdscr)
    elif choice == "3":
        markManagement.displayAllMarks(stdscr)
    elif choice == "4":
        markManagement.setStudents(stdscr)
    elif choice == "5":
        markManagement.setCourses(stdscr)
    elif choice == "6":
        markManagement.setMarks(stdscr)
    elif choice == "7":
        markManagement.searchStudent(stdscr)
    elif choice == "8":
        markManagement.searchCourse(stdscr)

class loadThread(threading.Thread):
    def __init__(self, markManagement, stdscr):
        threading.Thread.__init__(self)
        self.__markManagement = markManagement
        self.__stdscr = stdscr
    def run(self):
        if os.path.exists("students.dat.zip"):
            try:
                with zipfile.ZipFile("students.dat.zip", "r") as zipf:
                    zipf.extractall(".")

                self.__markManagement.loadFiles()
                
                self.__stdscr.addstr(30, 0, "Background thread: Data loaded successfully!", curses.A_BOLD)
                self.__stdscr.refresh()
            except Exception as e:
                self.__stdscr.clear()
                self.__stdscr.addstr(f"Error loading data!: {str(e)}")
                self.__stdscr.refresh()
                return