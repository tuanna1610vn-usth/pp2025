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
    course = {"name": name, "ID": id, "students": []}
    return course
    

def grade_input(course, student):
    ID = student["ID"]
    student_name = student["name"]
    course_id = course["ID"]
    gpa = float(input(f"Input student {student_name}'s GPA for {course_id}: "))
    course["students"].extend([{"ID": ID, "name": student_name, "Mark": gpa}])

def chooseCourse(courses, students):
    # Arguments: the list of courses and list of students
    course_found = False
    course_name = input("Please enter a course name: ")
    for course in courses:
        if course_name == course["name"]:
            course_found = True
            for student in students:
                grade_input(course, student)
        else:
            continue
    if course_found:
        print("Student's mark successfully entered!")
    else:
        print(f"No course with name {course_name} was founded! Try again!")

def showCourseInfo(course):
    for record in course:
        print(f"Student result for {record["name"]}: ")
        for student in record["students"]:
            print(student, ", GPA: ", student["Mark"])

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

#for course in courses:
#    for student in students:
#        grade_input(course, student)
chooseCourse(courses, students)
showCourseInfo(courses)