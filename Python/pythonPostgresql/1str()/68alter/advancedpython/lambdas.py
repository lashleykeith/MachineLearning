def alter(values, check):
    #return list(filter(check,values))
    return [val for val in values if check(val)]

def remove_numbers(value):
    return alter(value, lambda x: x not in [str(n) for n in range(10)])

def skip_letter(value, letter):
    return alter(value, lambda x: x != letter )

def add_letter(value, letter):
    return alter(value, lambda x: x == letter)


print(remove_numbers("hel5lo"))
print(skip_letter("hello", "e"))
print(add_letter("hello","e"))

'''
#regular function
def sum(x,y):
	return x + y
print(sum(1,3))

#lambda function
sum = lambda x,y: x + y
print(sum(5,10))
'''