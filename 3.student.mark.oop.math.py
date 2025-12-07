import math
import numpy as np

class Student:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__dob = None
    
    # Setter and Getter
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
    
    # Input method
    def input(self):
        name = input("Enter student name: ")
        id = input("Enter student ID: ")
        dob = input("Enter student's date of birth: ")
        self.setID(id)
        self.setName(name)
        self.setDOB(dob)

    # Display method
    def display(self):
        print(f"Name: {self.getName()} | ID: {self.getID()} | DOB: {self.getDOB()}")

class Course:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__credits = None
    
    # Setter and Getter
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
    
    # Input method
    def input(self):
        name = input("Enter course name: ")
        id = input("Enter course ID: ")
        credits = int(input("Enter number of credits: "))
        self.setID(id)
        self.setName(name)
        self.setCredit(credits)

    # Display method
    def display(self):
        print(f"Course name: {self.getName()} | ID: {self.getID()}")

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
    
    def input(self, student, course):
        self.setStudent(student)
        self.setCourse(course)
        gpa = float(input(f"Enter {student.getName()}'s GPA for {course.getName()}: "))
        self.setMark(math.floor(gpa))
    
    def display(self):
        print(f"Course: {self.__course.getName()}"
              f"| Name: {self.__student.getName()}"
              f"| ID: {self.__student.getID()}"
              f"| Result: {self.getMark()}")

class mark_management:
    def __init__(self):
        self.__courses = None
        self.__students = None
        self.__marks = None

    def setCourses(self):
        self.__courses = []
        n = int(input("Enter the number of courses: "))
        for i in range(n):
            print(f"Course number #{i+1}: ")
            c = Course()
            c.input()
            self.__courses.append(c)
    def getCourses(self):
        return self.__courses
    
    def setStudents(self):
        self.__students = []
        n = int(input("Enter the number of students: "))
        for i in range(n):
            print(f"Student number #{i+1}: ")
            s = Student()
            s.input()
            self.__students.append(s)
    def getStudents(self):
        return self.__students

    def setMarks(self, course):
        print(f"Enter students' mark for {course.getName()}: ")
        for s in self.__students:
            m = Mark()
            m.input(s, course)
            self.__marks.append(m)
    def getMarks(self):
        return self.__marks
    
    def input(self):
        self.__marks = []
        self.setStudents()
        self.setCourses()
        for c in self.__courses:
            self.setMarks(c)

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

    def rankings(self):
        student_results = self.calGPA()
        ranked = sorted(student_results, key=lambda x: x["Average GPA"], reverse=True)

        print("-" * 50)
        print("Student Rankings by GPA: ")

        i = 1
        for r in ranked:
            print(f"{i}. Student ID: {r["ID"]} | Name: {r["Name"]} | GPA: {r["Average GPA"]}")
            i += 1


    def display(self):
        print("-" * 50)
        print("All courses' informations: ")
        for c in self.__courses:
            c.display()
        
        print("-" * 50)
        print("All students' informations: ")
        for s in self.__students:
            s.display()
        
        print("-" * 50)
        print("Students' result for the class: ")
        for m in self.__marks:
            m.display()

mm = mark_management()
mm.input()
mm.display()
mm.rankings()