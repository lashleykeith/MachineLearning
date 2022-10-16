>>> numbers = [3,16,7,4,3,3,3]
>>> numbers
[3, 16, 7, 4, 3, 3, 3]
>>> numbers = set()
>>> numbers
set()
>>> numbers.add(3)
>>> numbers
{3}
>>> numbers.add(3)
>>> numbers
{3}
>>> numbers.add(2)
>>> numbers
{2, 3}
>>> lottery_values = {3,5,17,6}
>>> lottery_values
{17, 3, 5, 6}
>>> user_values = {3,5,11,2}
>>> user_values
{11, 2, 3, 5}
>>> lottery_values.intersection(user_values)
{3, 5}
>>> user_values.intersection(lottery_values)
{3, 5}
>>> 