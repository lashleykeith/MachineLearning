"""
This script create an empty file.
"""

filename = "cake.txt"

#Create empty file
def create_file():
	"""This function creates an empty file"""
	with open(filename,"w") as file:
		file.write("")