
'''
#regular function
def sum(x,y):
	return x + y
print(sum(1,3))

#lambda function
sum = lambda x,y: x + y
print(sum(5,10))
'''

l = lambda x: x > 5
print(l(10))

def alter(values, check):
    return [val for val in values if check(val)]

my_list = [1,2,3,4,5]

def check_not_five(x):
    return x != 5

another_list = alter(my_list, check_not_five)

print(another_list)
