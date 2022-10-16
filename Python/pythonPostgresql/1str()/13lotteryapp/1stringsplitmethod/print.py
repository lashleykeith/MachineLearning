>>> numbers = "4,2,6,7,8"
>>> numbers
'4,2,6,7,8'
>>> numbers.split(",")
['4', '2', '6', '7', '8']
>>> user_numbers = input("Enter your numbers, seperated by commas: ")
Enter your numbers, seperated by commas: 1,34,5,,6,7
>>> user_numbers.split(",")
['1', '34', '5', '', '6', '7']
>>> 