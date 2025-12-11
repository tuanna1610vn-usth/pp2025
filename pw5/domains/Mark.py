import math
import curses

class Mark:
    def __init__(self):
        self.__gpa = None
        self.__student = None
        self.__course = None
    
    def setMark(self, gpa):
        self.__gpa = gpa
    def getMark(self):
        return self.__gpa
    
    def setStudent(self, student):
        self.__student = student
    def getStudent(self):
        return self.__student
    
    def setCourse(self, course):
        self.__course = course
    def getCourse(self):
        return self.__course
    
    def input(self, student, course, stdscr, y):
        curses.echo()
        self.setStudent(student)
        self.setCourse(course)

        stdscr.addstr(y, 0, f"Enter {student.getName()}'s GPA for {course.getName()}: ")
        gpa = float(stdscr.getstr(y, 70, 6).decode('utf-8'))
        self.setMark(math.floor(gpa))
        curses.noecho()
    
    def display(self):
        return (f"Course: {self.__course.getName()}"
              f"| Name: {self.__student.getName()}"
              f"| ID: {self.__student.getID()}"
              f"| Result: {self.getMark()}")