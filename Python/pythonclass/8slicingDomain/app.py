email = input("enter you email ID? ")


username = email[:email.index("@"):]

domain = email[email.index("@") +1:email.index("."):]

print("hey your name is {} and your email domain is {}".format(username,domain))