# Learning Management System - Version 2.0

courses = ["Python", "DBMS", "Computer Networks"]

def display_courses():
    print("Available Courses:")
    for course in courses:
        print(course)

def enroll_student(student, course):
    print(student, "enrolled in", course)

def submit_assignment(student, assignment):
    print(student, "submitted", assignment)

def give_result(student, course, marks):
    print(student, "scored", marks, "in", course)

display_courses()
enroll_student("Student1", "Python")
submit_assignment("Student1", "Python Assignment")
give_result("Student1", "Python", 85)
