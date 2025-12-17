import os
import curses
import pickle
import numpy as np
from . import Course
from . import Mark
from . import Student

class markManagement:
    def __init__(self):
        self.__courses = []
        self.__students = []
        self.__marks = []

    def setCourses(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, "===== COURSE SETUP =====", curses.A_BOLD)
        stdscr.addstr(2, 0, "Enter the number of courses: ")
        n = int(stdscr.getstr(2, 30, 2).decode('utf-8'))
        curses.noecho()

        for i in range(n):
            c = Course.Course()
            c.input(stdscr)
            self.__courses.append(c)
    def getCourses(self):
        return self.__courses
    
    def setStudents(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, "===== STUDENT SETUP =====", curses.A_BOLD)
        stdscr.addstr(2, 0, "Enter the number of students: ")
        n = int(stdscr.getstr(2, 30, 2).decode('utf-8'))
        curses.noecho()

        for i in range(n):
            s = Student.Student()
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
            # If a student and their courses' mark already exist in the file, then skip
            if os.path.exists("marks.bin"):
                duplicated = False
                with open("marks.bin", "rb") as f:
                    marks = pickle.load(f)
                    for m in marks:
                        if m.getStudent().getID() == s.getID() and m.getCourse().getID() == course.getID():
                            duplicated = True
                            break
                if duplicated:
                    continue
                else:
                    m = Mark.Mark()
                    m.input(s, course, stdscr, y)
                    self.__marks.append(m)
                    y += 1
            else:
                m = Mark.Mark()
                m.input(s, course, stdscr, y)
                self.__marks.append(m)
                y += 1
    def getMarks(self):
        return self.__marks
    
    def input(self, stdscr):
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
    
    def loadFiles(self):
        if os.path.exists("students.bin") and os.path.exists("courses.bin") and os.path.exists("marks.bin"):
            with open("students.bin", "rb") as f:
                students = pickle.load(f)
                for s in students:
                    self.__students.append(s)
            with open("courses.bin", "rb") as f:
                courses = pickle.load(f)
                for c in courses:
                    self.__courses.append(c)
            with open("marks.bin", "rb") as f:
                marks = pickle.load(f)
                for m in marks:
                    self.__marks.append(m)
        else:
            pass
    
    def saveFiles(self):
        with open("students.bin", "wb") as f:
            pickle.dump(self.__students, f)
        with open("courses.bin", "wb") as f:
            pickle.dump(self.__courses, f)
        with open("marks.bin", "wb") as f:
            pickle.dump(self.__marks, f)