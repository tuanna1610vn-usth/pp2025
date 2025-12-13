import curses

class Student:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__dob = None
    
    def setID(self, id):
        self.__id = id
    def getID(self):
        return self.__id
    
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    
    def setDOB(self, dob):
        self.__dob = dob
    def getDOB(self):
        return self.__dob
    
    def input(self, stdscr):
        curses.echo() # Enables showing characters from user input
        stdscr.clear()
        stdscr.addstr(0, 0, "===== ADD STUDENTS IN CLASS =====", curses.A_BOLD)

        stdscr.addstr(4, 0, "Enter student name: ")
        name = stdscr.getstr(4, 20, 30).decode('utf-8')
        stdscr.addstr(5, 0, "Enter student ID: ")
        id = stdscr.getstr(5, 20, 30).decode('utf-8')
        stdscr.addstr(6, 0, "Enter student's date of birth: ")
        dob = stdscr.getstr(6, 31, 30).decode('utf-8')

        self.setID(id)
        self.setName(name)
        self.setDOB(dob)
        curses.noecho()

    def display(self):
        return f"Name: {self.getName()} | ID: {self.getID()} | DOB: {self.getDOB()}"