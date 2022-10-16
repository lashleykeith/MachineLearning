def create_student():
	name = input("Please enter the new student's name: ")
	student_data = {
		'name':name,
		'marks':[]
	}

	return student_data

s = create_student()

def add_mark(student, mark):
	student['marks'].append(mark)

add_mark(s, 5) # Passing by reference


print(s)