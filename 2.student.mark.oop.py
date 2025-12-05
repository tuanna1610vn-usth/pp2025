class Student:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__DoB = None
    def setID(self, ID):
        self.ID = ID
    def getID(self):
        return self.ID
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setDoB(self, DoB):
        self.DoB = DoB
    def getDoB(self):
        return self.DoB
    
class Course:
    def __init__(self):
        self.__id = None
        self.__name = None
        self.__students = None
    def setID(self, ID):
        self.ID = ID
    def getID(self):
        return self.ID
    def setName(self, name):
        self.name = name
    def getName(self):
        return self.name
    def setMark(self, students):
        self.students = students
        for student in self.students:
            gpa = float(input(f"Enter student {student["Student"].getID()}'s GPA for {self.getID()}: "))
            student["GPA"] = gpa
    def getMark(self):
        print(f"Student's information on {self.getName()}: ")
        for student in self.students:
            print(f"Name: {student["Student"].getName()}")
            print(f"Student ID: {student["Student"].getID()}")
            print(f"Date of birth: {student["Student"].getDoB()}")
            print(f"GPA: {student["GPA"]}")
    
def setStudent():
    n = int(input("Enter the number of students in class: "))
    students = []
    for i in range(0, n):
            student = Student()
            sName = input(f"Enter student #{i+1}'s name: ")
            sID = input(f"Enter student #{i+1}'s ID: ")
            sDoB = input(f"Enter student #{i+1}'s birthday: ")
            student.setName(sName)
            student.setID(sID)
            student.setDoB(sDoB)
            students.extend([{"Student": student}])
    return students

def chooseCourse(courses, students):
    # Arguments: the list of courses and list of students
    course_found = False
    course_name = input("Enter a course name to input student's mark: ")
    for course in courses:
        if course_name == course.getName():
            course_found = True
            course.setMark(students)
        else:
            continue
    if course_found:
        print("Student's mark successfully entered!")
    else:
        print(f"No course with name {course_name} was founded! Try again!")

def showResult(courses, students):
    print("Showing students' mark: ")
    course_found = False
    course_name = input("Enter course name: ")
    for course in courses:
        if course_name == course.getName():
            course_found = True
            course.getMark()
        else:
            continue
    if course_found:
        print("Done!")
    else:
        print(f"No course with name {course_name} was founded! Try again!")

students = setStudent()
courses = []
n = int(input("Enter the number of courses: "))
for i in range(0, n):
    course = Course()
    name = input(f"Enter course #{i+1}'s name: ")
    course.setName(name)
    ID = input(f"Enter course #{i+1}'s ID: ")
    course.setID(ID)
    courses.extend([course])

chooseCourse(courses, students)
showResult(courses, students)