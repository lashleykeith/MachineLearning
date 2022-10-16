#import numpy as np
student_list = [] 
 
class Student:
    def __init__(self):
        self.name = "John"
        self.marks = []
 
def create_student():
    name = input("Enter student name: ")
    profile = Student()
    return profile
    
def add_mark(student, mark):
    student.marks.append(mark)
    
def calc_avg(student):
    if len(student.marks) == 0:
        return 0
    avg = np.mean(student.marks)
    return avg
    
def single_student_detail(student):
    print(student.name, student.marks, calc_avg(student))
    
def all_student_detail(student): # student_list
    for i, student in enumerate(student): #student_list
        print("ID: ", i)
        single_student_detail(student)
        
def menu():
    selection = input("Enter p for list of students, s to add student, a to add marks, q to quit. ENTER SELECTION: ")
    while selection != 'q':
        if selection == 'p':
            all_student_detail(student_list)
        if selection == 's':
            student_list.append(create_student())
            print(student_list) # this is a list of dictionaries
        if selection =='a':
            student_id = int(input("Enter student id: "))
            student_mark = int(input("Enter student mark: "))
            student = student_list[student_id]
            add_mark(student, student_mark)
        selection = input("Enter p for list of students, s to add student, a to add marks, q to quit. ENTER SELECTION: ")
menu()