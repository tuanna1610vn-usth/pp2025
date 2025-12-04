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
    def setStudent(self, students):
        self.students = students
        for student in self.students:
            gpa = float(input(f"Enter student {student["Name"]}'s GPA for {self.getID()}: "))
            student["GPA"] = gpa
    def getStudent(self):
        return self.students
    
def setNumStudent():
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
            students.extend([{"ID": student.getID(), "Name": student.getName(), "DoB": student.getDoB()}])
    return students

Math = Course()
Math.setID(123)
Math.setName("Mathematics")
students = setNumStudent()
Math.setStudent(students)
print(Math.getStudent())