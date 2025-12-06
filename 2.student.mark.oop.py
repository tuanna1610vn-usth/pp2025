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
    
    # Setter and Getter
    def setID(self, id):
        self.__id = id
    def getID(self):
        return self.__id
    
    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name
    
    # Input method
    def input(self):
        name = input("Enter course name: ")
        id = input("Enter course ID: ")
        self.setID(id)
        self.setName(name)

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
        self.setMark(gpa)
    
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
        print("All courses' informations: ")
        for c in self.__courses:
            c.display()
    
    def setStudents(self):
        self.__students = []
        n = int(input("Enter the number of students: "))
        for i in range(n):
            print(f"Student number #{i+1}: ")
            s = Student()
            s.input()
            self.__students.append(s)
    def getStudents(self):
        print("All students' informations: ")
        for s in self.__students:
            s.display()

    def setMarks(self, course):
        # Set the mark of students for 1 particular course
        self.__marks = []
        print(f"Enter students' mark for {course.getName()}: ")
        for s in self.__students:
            m = Mark()
            m.input(s, course)
            self.__marks.append(m)
    def getMarks(self):
        print("Students' result for the class: ")
        for m in self.__marks:
            m.display()
    
    def input(self):
        self.setStudents()
        self.setCourses()

        # Choose 1 course to input students' mark
        founded = False
        course_name = input("Enter a course name to input marks: ")
        for c in self.__courses:
            if course_name.upper() == c.getName().upper():
                founded = True
                self.setMarks(c)
            else:
                continue
        if founded:
            print("Done!")
        else:
            print(f"No course with name {course_name} was founded, please try again!")


    def display(self):
        self.getCourses()
        self.getStudents()
        self.getMarks()

mm = mark_management()
mm.input()
mm.display()