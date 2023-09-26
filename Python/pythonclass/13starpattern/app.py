'''
n = int(input("Enter number of rows: "))

for i in range(n,0, -1):
	print((n - i) * '' + i * '*')
'''
'''
print(12, end = " @ ")

print("1,2,3", end = " $ ")
'''

num = 1
n = int(input("value of n: "))

for i in range(0,n):
	num = 1
	for j in range(0, i + 1):
		print(num, end = " ")
		num = num + 1

	print("\r")