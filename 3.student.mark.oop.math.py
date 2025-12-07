import math
import numpy as np
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
        gpa = float(stdscr.getstr(y, 50, 6).decode('utf-8'))
        self.setMark(math.floor(gpa))
        curses.noecho()
    
    def display(self):
        return (f"Course: {self.__course.getName()}"
              f"| Name: {self.__student.getName()}"
              f"| ID: {self.__student.getID()}"
              f"| Result: {self.getMark()}")

class mark_management:
    def __init__(self):
        self.__courses = None
        self.__students = None
        self.__marks = None

    def setCourses(self, stdscr):
        self.__courses = []

        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, "===== COURSE SETUP =====", curses.A_BOLD)
        stdscr.addstr(2, 0, "Enter the number of courses: ")
        n = int(stdscr.getstr(2, 30, 2).decode('utf-8'))
        curses.noecho()

        for i in range(n):
            c = Course()
            c.input(stdscr)
            self.__courses.append(c)
    def getCourses(self):
        return self.__courses
    
    def setStudents(self, stdscr):
        self.__students = []

        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, "===== STUDENT SETUP =====", curses.A_BOLD)
        stdscr.addstr(2, 0, "Enter the number of students: ")
        n = int(stdscr.getstr(2, 30, 2).decode('utf-8'))
        curses.noecho()

        for i in range(n):
            s = Student()
            s.input(stdscr)
            self.__students.append(s)
    def getStudents(self):
        return self.__students

    def setMarks(self, course, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, f"Enter students' mark for {course.getName()}: ", curses.A_BOLD | curses.A_UNDERLINE)
        stdscr.addstr(1, 0, "-" * 100)

        y = 3
        for s in self.__students:
            m = Mark()
            m.input(s, course, stdscr, y)
            self.__marks.append(m)
            y += 1
    def getMarks(self):
        return self.__marks
    
    def input(self, stdscr):
        self.__marks = []

        stdscr.clear()
        title = "STUDENT MANAGEMENT SYSTEM"
        stdscr.addstr(10, 15, title, curses.A_BOLD | curses.A_REVERSE)
        stdscr.addstr(12, 15, "Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()

        self.setStudents(stdscr)
        self.setCourses(stdscr)
        for c in self.__courses:
            self.setMarks(c, stdscr)

    def calGPA(self):
        student_results = []

        for s in self.__students:
            avg_GPA = 0
            GPAs = []
            credits = []

            for m in self.__marks:
                if s.getID() == m.getStudent().getID():
                    GPAs.append(m.getMark())
                    credits.append(m.getCourse().getCredit())

            for i in range(len(GPAs)):
                avg_GPA += GPAs[i] * credits[i]

            credits_arr = np.array(credits)
            avg_GPA = float(avg_GPA / credits_arr.sum())
            student_results.append({"ID": s.getID(), "Name": s.getName(), "Average GPA": avg_GPA})

        return student_results

    def rankings(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "===== STUDENT RANKINGS BY GPA =====", curses.A_BOLD)
        stdscr.addstr(1, 0, "-" * 50)

        student_results = self.calGPA()
        ranked = sorted(student_results, key=lambda x: x["Average GPA"], reverse=True)

        i = 1
        for r in ranked:
            stdscr.addstr(i+1, 0, f"{i}. Student ID: {r["ID"]} | Name: {r["Name"]} | GPA: {r["Average GPA"]}", curses.A_BOLD)
            i += 1
        
        stdscr.addstr(i+1, 0, "-" * 50)
        stdscr.addstr(i+2, 0, "Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()


    def display(self, stdscr):
        stdscr.clear()
        stdscr.addstr(0, 0, "===== ALL COURSES' INFORMATION =====", curses.A_BOLD)
        stdscr.addstr(1, 0, "-" * 50)
        y = 3
        for c in self.__courses:
            stdscr.addstr(y, 0, c.display())
            y += 1
        stdscr.addstr(y + 1, 0, "Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()
        
        stdscr.clear()
        stdscr.addstr(0, 0, "===== ALL STUDENTS' INFORMATION =====", curses.A_BOLD)
        stdscr.addstr(1, 0, "-" * 50)
        y = 3
        for s in self.__students:
            stdscr.addstr(y, 0, s.display())
            y += 1
        stdscr.addstr(y + 1, 0, "Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()
        
        stdscr.clear()
        stdscr.addstr(0, 0, "===== STUDENTS' RESULT =====", curses.A_BOLD)
        stdscr.addstr(1, 0, "-" * 50)
        y = 3
        for m in self.__marks:
            stdscr.addstr(y, 0, m.display())
            y += 1
        stdscr.addstr(y + 1, 0, "Press any key to continue...")
        stdscr.refresh()
        stdscr.getch()

def main(stdscr):
    curses.curs_set(1)
    mm = mark_management()
    mm.input(stdscr)
    mm.display(stdscr)
    mm.rankings(stdscr)

    stdscr.clear()
    exit = "Thank you for using Student Management System!"
    stdscr.addstr(10, 15, exit, curses.A_BOLD)
    stdscr.addstr(12, 15, "Press any key to exit...")
    stdscr.refresh()
    stdscr.getch()

curses.wrapper(main)