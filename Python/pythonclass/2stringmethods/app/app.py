
name = input("What is your name? ")

age = 35
print("Your name is {0} and your age is {1}".format(name, age))


age = input("Enter your age: ")
print("You have lived for {} seconds.  This corresponds to {} years.".format(int(age) * 365 * 24 * 60 * 60, age))