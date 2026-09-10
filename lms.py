# Learning Management System - Version 1.0

courses = ["Python", "DBMS", "Computer Networks"]

def display_courses():
    print("Available Courses:")
    for course in courses:
        print(course)

def enroll_student(student, course):
    print(student, "enrolled in", course)

display_courses()
enroll_student("Student1", "Python")
