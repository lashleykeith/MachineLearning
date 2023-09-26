weather = input("How is the weather?  Is it Sunny, Rainy or Snowy ")

if(weather == "Sunny"):
	print("weather is nice")
elif(weather == "Snowy"):
	print("weather is cold")
elif(weather == "Rainy"):
	print("weather is rainy")
else:
	print("Don't know")



people = int(input("Number of people"))
bunnies = 100
if people > bunnies:
	print("There are more people than bunnies")
elif people == bunnies:
	print("People and Bunnies are they same")