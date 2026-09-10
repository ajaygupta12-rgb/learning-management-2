# Learning Management System - Version 1.1

courses = ["Python", "DBMS", "Computer Networks"]

def display_courses():
    print("Available Courses:")
    for course in courses:
        print(course)

def enroll_student(student, course):
    print(student, "enrolled in", course)

def submit_assignment(student, assignment):
    print(student, "submitted", assignment)

display_courses()
enroll_student("Student1", "Python")
submit_assignment("Student1", "Python Assignment")
