import curses

class Course:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__credits = None
    
    def setID(self, id):
        self.__id = id
    def getID(self):
        return self.__id
    
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    
    def setCredit(self, credits):
        self.__credits = credits
    def getCredit(self):
        return self.__credits
    
    def input(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, "===== ADD COURSES =====", curses.A_BOLD)

        stdscr.addstr(4, 0, "Enter course name: ")
        name = stdscr.getstr(4, 20, 30).decode('utf-8')
        stdscr.addstr(5, 0, "Enter course ID: ")
        id = stdscr.getstr(5, 20, 30).decode('utf-8')
        stdscr.addstr(6, 0, "Enter number of credits: ")
        credits = stdscr.getstr(6, 31, 30).decode('utf-8')

        self.setID(id)
        self.setName(name)
        self.setCredit(int(credits))
        curses.noecho()

    def display(self):
        return f"Course name: {self.getName()} | ID: {self.getID()}"