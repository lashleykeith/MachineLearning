class Account:

	def __init__(self, filepath):
		self.filepath=filepath
		with open(filepath, 'r') as file:
			self.balance=int(file.read())
#you have to do this from the commandline if you use account//balance.txt
#you don't if just used balance.txt

	def withdraw(self, amount):
		self.balance=self.balance - amount

	def deposit(self, amount):
		self.balance=self.balance + amount

	def commit(self):
		with open(self.filepath, 'w') as file:
			file.write(str(self.balance))

class Checking(Account):
	"""This class generates checking account objects"""

	type="checking"

	def __init__(self, filepath, fee):
		Account.__init__(self, filepath)
		self.fee=fee

	def transfer(self,amount):
		self.balance=self.balance-amount - self.fee

jacks_checking=Checking("jack.txt",1)
#or try checking=Checking("account\\jack.txt")
jacks_checking.transfer(100)
print(jacks_checking.balance)
jacks_checking.commit()
print(jacks_checking.type)

johns_checking=Checking("john.txt",1)
#or try checking=Checking("account\\john.txt")
johns_checking.transfer(100)
print(johns_checking.balance)
johns_checking.commit()
print(johns_checking.type)

print(johns_checking.__doc__)