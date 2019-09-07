class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount
    	return self	# the specific user's account increases by the amount of the value received
    def make_withdrawal(self,amount):
    	self.account_balance -= amount
    	return self
    def display_user_balance(self):
    	print("Name:",self.name)
    	print("Email:",self.email)
    	print("Account balance:",self.account_balance)
    	return self
    def transfer_money(self,other_user, amount):
    	self.account_balance -=amount
    	other_user.account_balance+=amount
    	return self


class BankAccount:
	def __init__(self, int_rate, balance):
		self.int_rate = int_rate
		self.balance = balance
	 # don't forget to add some default values for these parameters!
		# your code here! (remember, this is where we specify the attributes for our class)
		# don't worry about user info here; we'll involve the User class soon
		print(self.balance)
	def deposit(self, amount):
		self.balance +=amount
		print(self.balance)
		return self
		# your code here
	def withdraw(self, amount):
		
		if self.balance<0:
			print("Insufficient funds: Charging a $5 fee")
			self.balance-=5
		else: 
			self.balance -=amount
		print(self.balance)
		return self
		
		# your code here
	def display_account_info(self):
		print("Your balance is:",self.balance)
		return self
		# your code here
	def yield_interest(self):
		self.balance += self.balance*(self.int_rate/100)
		return self
		# your code here

#chase = BankAccount(10,100)
bofa = BankAccount(1,10)

#chase.deposit(100).deposit(1000).deposit(5).withdraw(5).yield_interest().display_account_info()
bofa.deposit(50).deposit(50).withdraw(100).withdraw(100).withdraw(10).withdraw(1).yield_interest().display_account_info()

#guido = User('archana', 'myemail@gmail.com')
#monty = User('Michael', 'mbrower@apple.com')
#guido.make_deposit(100)
#guido.make_deposit(200)
#monty.make_deposit(50)
#print(guido.account_balance)	# output: 300
#print(monty.account_balance)	# output: 50
#guido.make_withdrawal(1000)
#print(guido.account_balance)
#guido.transfer_money(monty,150)
#guido.display_user_balance()

#guido.make_deposit(100).make_deposit(200).make_deposit(300).make_withdrawal(50).display_user_balance()


	# output: 300





#For this assignment, we'll add some functionality to the User class:
#make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
#display_user_balance(self) - have this method print the user's name and account balance to the terminal
#eg. "User: Guido van Rossum, Balance: $150
#BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount 
#and add that amount to other other_user's balance


