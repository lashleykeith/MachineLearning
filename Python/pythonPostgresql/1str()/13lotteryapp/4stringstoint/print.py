# User can pick 6 numbers
# Lottery calculates 6 random numbers (between 1 and 20)
# Then we match the user numbers to lottery numbers
# Calculate the winnings based on how many numbers the user matched

def get_player_numbers():
	number_csv = input("Enter your 6 numbers, seperated by commas:")
	#Now, I want to create a set of integers from this number_csv
	number_list = number_csv.split(",") #['1','2','3']
	integer_set = {int(number) for number in number_list}
	return integer_set

print(get_player_numbers())

