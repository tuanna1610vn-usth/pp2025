def setNumStudent():
    n = int(input("Input the number of students: "))
    return n

def setInfoStudent(position):
    id = input(f"Input student #{position}'s ID: ")
    name = input(f"Input student #{position}'s name: ")
    DoB = input(f"Input student #{position}'s date of birth: ")
    student = {"name": name, "ID": id, "DoB" : DoB}
    return student

def setNumCourse():
    n = int(input("Input the number of courses: "))
    return n

def setInfoCourse(position):
    id = input(f"Input course #{position}'s ID: ")
    name = input(f"Input course #{position}'s name: ")
    course = {"name": name, "ID": id}
    return course

nStudent = setNumStudent()
students = []

for i in range(0, nStudent):
    x = setInfoStudent(i+1)
    students.extend([x])

for record in students:
    print(record)

nCourse = setNumCourse()
courses = []

for i in range(0, nCourse):
    x = setInfoCourse(i+1)
    courses.extend([x])

for record in courses:
    print(record)