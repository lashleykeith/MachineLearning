import random

# User can pick 6 numbers

def get_player_numbers():
	number_csv = input("Enter your 6 numbers, seperated by commas:")
	#Now, I want to create a set of integers from this number_csv
	number_list = number_csv.split(",") #['1','2','3']
	integer_set = {int(number) for number in number_list}
	return integer_set

# Lottery calculates 6 random numbers (between 1 and 20)
def create_lottery_numbers():
	values = set() # Cannot initialize like so: {}
	while len(values) < 6: # range in [0,1,2,3,4,5]
		values.add(random.randint(1,20))
	return values
# Then we match the user numbers to lottery numbers
# Calculate the winnings based on how many numbers the user matched

print(create_lottery_numbers())