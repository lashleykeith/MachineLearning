>>> user_input = "1,2,3,4,5,6"
>>> user_numbers = user_input.split(",")
>>> user_numbers
['1', '2', '3', '4', '5', '6']
>>> user_numbers_as_int = []
>>> for number in user_numbers:
	user_numbers_as_int.append(int(number))

	
>>> user_numbers_as_int
[1, 2, 3, 4, 5, 6]
>>> [number for number in user_numbers]
['1', '2', '3', '4', '5', '6']
>>> [number*2 for number in user_numbers]
['11', '22', '33', '44', '55', '66']
>>> [int(number) for number in user_numbers]
[1, 2, 3, 4, 5, 6]
>>> user_input = "1,2,3,4,5,6"
>>> user_numbers = user_input.split(",")
>>> user_numbers
['1', '2', '3', '4', '5', '6']
>>> user_numbers_as_int = []
>>> for number in user_numbers:
	user_numbers_as_int.append(int(number))

	
>>> user_numbers_as_int
[1, 2, 3, 4, 5, 6]
>>> 