import time
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

    def setMarks(self, stdscr):
        curses.echo()
        stdscr.clear()
        stdscr.addstr(0, 0, "Find a course to input students' mark: ")
        cName = stdscr.getstr(0, 40).decode("utf-8").strip()
        stdscr.refresh()
        founded = False
        course = None
        for c in self.__courses:
            if cName.lower() in c.getName().lower():
                course = c
                founded = True
                break
        if founded:
            stdscr.clear()
            stdscr.addstr(0, 0, f"Enter students' mark for {course.getName()}: ", curses.A_BOLD | curses.A_UNDERLINE)
            stdscr.addstr(1, 0, "-" * 100)
            stdscr.refresh()

            y = 3
            for s in self.__students:
                # If a student and their courses' mark already exist in the file, then skip
                if os.path.exists("marks.bin"):
                    duplicated = False
                    with open("marks.bin", "rb") as f:
                        marks = pickle.load(f)
                        for m in marks:
                            if m.getStudent().getID() == s.getID() and m.getCourse().getName() == course.getName():
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
            stdscr.clear()
            stdscr.addstr(3, 0, f"All students have got their mark in {course.getName()}!")
            stdscr.addstr(4, 0, "Press any key to continue...")
            stdscr.refresh()
            stdscr.getch()
        else:
            stdscr.addstr(1, 0, "Course not founded! Press any key to go back...")
            stdscr.refresh()
            stdscr.getch()
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
    
    def displayAllStudents(self, stdscr):
        if len(self.__students) == 0:
            stdscr.clear()
            stdscr.addstr(25, 50, "Error: The list of student is now empty", curses.A_BOLD)
            stdscr.addstr(25, 50, "Press any key to go back...")
            stdscr.refresh()
            stdscr.getch()
        else:
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
    
    def displayAllCourses(self, stdscr):
        if len(self.__courses) == 0:
            stdscr.clear()
            stdscr.addstr(25, 50, "Error: The list of courses is now empty", curses.A_BOLD)
            stdscr.addstr(25, 50, "Press any key to go back...")
            stdscr.refresh()
            stdscr.getch()
        else:
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
    
    def displayAllMarks(self, stdscr):
        if len(self.__marks) == 0:
            stdscr.clear()
            stdscr.addstr(25, 50, "Error: The list of marks is now empty", curses.A_BOLD)
            stdscr.addstr(25, 50, "Press any key to go back...")
            stdscr.refresh()
            stdscr.getch()
        else:
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

    def searchStudent(self, stdscr):
        curses.echo()
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "===== SEARCH FOR STUDENT =====", curses.A_BOLD)
            stdscr.addstr(1, 0, "Choose your searching mode: ", curses.A_UNDERLINE)
            stdscr.addstr(2, 0, "1. By name")
            stdscr.addstr(3, 0, "2. By ID")
            stdscr.addstr(4, 0, "3. By name and ID")
            stdscr.addstr(5, 0, "0. Return")
            
            choice = stdscr.getkey()
            if choice == "0":
                break
            else:
                if choice == "1":
                    founded = False
                    i = 1
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Search student name: ")
                    name = stdscr.getstr(0, 30).decode("utf-8")
                    stdscr.refresh()
                    for s in self.__students:
                        if name.strip().lower() in s.getName().lower():
                            stdscr.addstr(i, 0, s.display(), curses.A_BOLD)
                            founded = True
                            i += 1
                    if founded:
                        stdscr.addstr(i+1, 0, "Press any key to continue...")
                        stdscr.refresh()
                        stdscr.getch()
                    else:
                        stdscr.addstr(1, 0, f"No student with name {name} was founded!")
                        stdscr.addstr(2, 0, "Press any key to continue")
                        stdscr.refresh()
                        stdscr.getch()
                elif choice == "2":
                    founded = False
                    i = 1
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Search student ID: ")
                    ID = stdscr.getstr(0, 30).decode("utf-8")
                    stdscr.refresh()
                    for s in self.__students:
                        if ID.strip().lower() in s.getID().lower():
                            stdscr.addstr(i, 0, s.display(), curses.A_BOLD)
                            founded = True
                            i += 1
                    if founded:
                        stdscr.addstr(i+1, 0, "Press any key to continue...")
                        stdscr.refresh()
                        stdscr.getch()
                    else:
                        stdscr.addstr(1, 0, f"No student with ID {ID} was founded!")
                        stdscr.addstr(2, 0, "Press any key to continue")
                        stdscr.refresh()
                        stdscr.getch()
                elif choice == "3":
                    founded = False
                    i = 2
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Search student name: ")
                    name = stdscr.getstr(0, 30).decode("utf-8")
                    stdscr.addstr(1, 0, "Search student ID: ")
                    ID = stdscr.getstr(1, 30).decode("utf-8")
                    stdscr.refresh()
                    for s in self.__students:
                        if ID.strip().lower() in s.getID().lower() and name.strip().lower() in s.getName().lower():
                            stdscr.addstr(i, 0, s.display(), curses.A_BOLD)
                            founded = True
                            i += 1
                    if founded:
                        stdscr.addstr(i+1, 0, "Press any key to continue...")
                        stdscr.refresh()
                        stdscr.getch()
                    else:
                        stdscr.addstr(2, 0, f"No student with name {name} and ID {ID} was founded!")
                        stdscr.addstr(3, 0, "Press any key to continue")
                        stdscr.refresh()
                        stdscr.getch()
                else:
                    stdscr.addstr(10, 0, "Error: You did not enter a valid key!")
                    stdscr.refresh()
                    time.sleep(3)

    def searchCourse(self, stdscr):
        curses.echo()
        while True:
            stdscr.clear()
            stdscr.addstr(0, 0, "===== SEARCH FOR COURSE =====", curses.A_BOLD)
            stdscr.addstr(1, 0, "Choose your searching mode: ", curses.A_UNDERLINE)
            stdscr.addstr(2, 0, "1. By name")
            stdscr.addstr(3, 0, "2. By ID")
            stdscr.addstr(4, 0, "3. By name and ID")
            stdscr.addstr(5, 0, "0. Return")
            
            choice = stdscr.getkey()
            if choice == "0":
                break
            else:
                if choice == "1":
                    founded = False
                    i = 1
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Search course name: ")
                    name = stdscr.getstr(0, 30).decode("utf-8")
                    stdscr.refresh()
                    for c in self.__courses:
                        if name.strip().lower() in c.getName().lower():
                            stdscr.addstr(i, 0, c.display(), curses.A_BOLD)
                            founded = True
                            i += 1
                    if founded:
                        stdscr.addstr(i+1, 0, "Press any key to continue...")
                        stdscr.refresh()
                        stdscr.getch()
                    else:
                        stdscr.addstr(1, 0, f"No course with name {name} was founded!")
                        stdscr.addstr(2, 0, "Press any key to continue")
                        stdscr.refresh()
                        stdscr.getch()
                elif choice == "2":
                    founded = False
                    i = 1
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Search course ID: ")
                    ID = stdscr.getstr(0, 30).decode("utf-8")
                    stdscr.refresh()
                    for c in self.__courses:
                        if ID.strip().lower() in c.getID().lower():
                            stdscr.addstr(i, 0, c.display(), curses.A_BOLD)
                            founded = True
                            i += 1
                    if founded:
                        stdscr.addstr(i+1, 0, "Press any key to continue...")
                        stdscr.refresh()
                        stdscr.getch()
                    else:
                        stdscr.addstr(1, 0, f"No course with ID {ID} was founded!")
                        stdscr.addstr(2, 0, "Press any key to continue")
                        stdscr.refresh()
                        stdscr.getch()
                elif choice == "3":
                    founded = False
                    i = 2
                    stdscr.clear()
                    stdscr.addstr(0, 0, "Search course name: ")
                    name = stdscr.getstr(0, 30).decode("utf-8")
                    stdscr.addstr(1, 0, "Search course ID: ")
                    ID = stdscr.getstr(1, 30).decode("utf-8")
                    stdscr.refresh()
                    for c in self.__courses:
                        if ID.strip().lower() in c.getID().lower() and name.strip().lower() in c.getName().lower():
                            stdscr.addstr(i, 0, c.display(), curses.A_BOLD)
                            founded = True
                            i += 1
                    if founded:
                        stdscr.addstr(i+1, 0, "Press any key to continue...")
                        stdscr.refresh()
                        stdscr.getch()
                    else:
                        stdscr.addstr(2, 0, f"No course with name {name} and ID {ID} was founded!")
                        stdscr.addstr(3, 0, "Press any key to continue")
                        stdscr.refresh()
                        stdscr.getch()
                else:
                    stdscr.addstr(10, 0, "Error: You did not enter a valid key!")
                    stdscr.refresh()
                    time.sleep(3)
    
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