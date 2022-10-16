student_list = []

def create_student():
	name = input("Please enter the new student's name: ")
	student_data = {
		'name':name,
		'marks':[]
	}

	return student_data

def add_mark(student, mark):
	student['marks'].append(mark)


def calculate_average_mark(student):
	number = len(student['marks'])
	if number == 0:
		return 0

	total = sum(student['marks'])
	return total/number

def print_student_details(student):
	print("{}, average mark: {}.".format(student['name'],
										calculate_average_mark(student)))
def print_student_list(student_list):
	for student in students:
		print_student_details(student)
