class Account:

	def __init__(self, filepath):
		with open(filepath, 'r') as file:
			self.balance=(file.read())
#you have to do this from the commandline if you use account//balance.txt
#you don't if just used balance.txt



account=Account("account//balance.txt")
print(account.balance)
