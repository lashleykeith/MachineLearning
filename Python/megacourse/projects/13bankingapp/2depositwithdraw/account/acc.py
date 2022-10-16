class Account:

	def __init__(self, filepath):
		with open(filepath, 'r') as file:
			self.balance=int(file.read())
#you have to do this from the commandline if you use account//balance.txt
#you don't if just used balance.txt

	def withdraw(self, amount):
		self.balance=self.balance - amount

	def deposit(self, amount):
		self.balance=self.balance + amount

account=Account("account//balance.txt")
print(account.balance)
account.withdraw(100)
print(account.balance)
