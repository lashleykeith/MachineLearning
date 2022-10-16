class Movie:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre

class Cake:
	def __init__(self, name, caketype):
		self.name = name
		self.caketype = caketype


my_cake = Cake("rose", "strawberry")

print(my_cake.name)
print(my_cake.caketype)