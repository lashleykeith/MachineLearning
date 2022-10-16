magic_numbers = [3,9]
chances = 3
for attempt in range(chances):  # range(changes) is [0, 1, 2]
	print("This is attempt {}".format(attempt))
	user_number = int(input("Enter a number between 0 and 9: "))
	if user_number in magic_numbers:
		print("You got the number right!")
	if user_number not in magic_numbers:
		print("You didn't quite get it.")