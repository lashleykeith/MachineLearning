
employee = {
	"Mary" : 24,
	"Peter": 36,
	"Dan": 43,
	"Samantha": 35
}

company = {
	"Facebook" : 16,
	"Google": 21,
	"Apple": 43,
	"Amazon": 25,
	"Microsoft": 44,
	"Netflix": 22
}


# print(employee)

# emp = employee["Mary"]
# print(emp)
# emp = employee["Peter"]
# print(emp)

employee.update({"employee": "Matthew"})
print(employee)
employee["Matthew"] = 40
print(employee)
# del employee["Peter"]
# print(employee)

company.update({"Microsoft":45})
print(company)


employee.popitem()
print(employee)

company.update({"Netflix": 22})
employeepop = employee.popitem()
print(employeepop)

# employeekey = employee.keys()
# employeevalue = employee.values()
# print(employee)
# print(employeekey)
# print(employeevalue)

# a = list(employee.keys())
# print(a)
# b = a[0]
# print(b)
