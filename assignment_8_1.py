###Define parent class
class BankAccount():
	
	def __init__(self, account_number, balance):
		self.account_number = account_number
		self.balance = balance
		
	def withdrawl(self):
		withdrawl_amount = float(input("How much would you like to withdraw from your account? "))
		self.balance = self.balance - withdrawl_amount
		print("Your new balance is $" + str(self.balance) + ".")
		
	def deposit(self):
		deposit_amount = float(input("How much would you like to deposit into your account? "))
		self.balance = self.balance + deposit_amount
		print("Your new balance is $" + str(self.balance) + ".")
		
	def getBalance(self):
		return "Your current account balance is $" + str(self.balance)

###Define child classes		
class CheckingAccount(BankAccount):
	
	def __init__(self, account_number, balance, fees, minimum_balance):
		BankAccount.__init__(self, account_number, balance)
		self.fees = fees
		self.minimum_balance = minimum_balance
		
	def deductFees(self):
		self.balance = self.balance - fees
		
	def checkMinimumBalance(self):
		if self.balance < self.minimum_balance:
			print("ALERT: Your account balance is below the minimum balance of $" + 
				str(self.minimum_balance) + ". Please add funds to your account.")
		
			
class SavingsAccount(BankAccount):
	
	def __init__(self, account_number, balance, interest_rate):
		BankAccount.__init__(self, account_number, balance)
		self.interest_rate = interest_rate
		
	def addInterest(self):
		interest_amount = float(self.balance * self.interest_rate)
		balance = self.balance + interest_amount
		return "Your savings account has accrued $" + str(interest_amount) + " in interest. Your new account balance is $" + str(balance) + "."

###Create dictionary to store class objects		
acct_dict = {}

###Create class instances
account_1234 = CheckingAccount(1234, 100, 5, 50)
account_5678 = SavingsAccount(5678, 100, 0.02)
account_8765 = CheckingAccount(8765, 25, 5, 50)
account_4321 = SavingsAccount(4321, 25, 0.02)

###Assign class instances to dictionary
acct_dict[account_1234.account_number] = account_1234
acct_dict[account_5678.account_number] = account_5678
acct_dict[account_8765.account_number] = account_8765
acct_dict[account_4321.account_number] = account_4321

input_account = 0

###Request account number from user, check for error
while True:
	
	try:
		input_account = int(input("Welcome to Brent's Bank. Please enter your account number:"))
		print("Your account number is " + str(acct_dict[input_account].account_number) + 
			" and your account balance is $" + str(acct_dict[input_account].balance) + ".")
		break
		
	except:
		print("\nThat is not a valid account number.")
		
user_account = str('account_' + str(input_account))

###Perform different function for checking vs. savings account	
###There's probably a better way to do this, maybe add an 
### 'account type' attribute in the class settings
if user_account == 'account_1234' or user_account == 'account_8765':
	acct_dict[input_account].checkMinimumBalance()
else:
	print(acct_dict[input_account].addInterest())

user_action = ''

###Request type of action from user, call withdraw/deposit/balance functions or exit program
while True:
		
	try:
		input_action = int(input("\nPlease type 1 to withdraw money, 2 to deposit money, 3 to check your balance, or 4 to exit the program: "))
		if input_action == 1:
			acct_dict[input_account].withdrawl()
			repeat_select = str(input("\nWould you like to make another transaction? "))
			if repeat_select.lower() == 'yes':
				continue
			else:
				print("Thank you for using Brent's Bank service. Goodbye. ")
				break
				
		elif input_action == 2:
			acct_dict[input_account].deposit()
			repeat_select = str(input("\nWould you like to make another transaction? "))
			if repeat_select.lower() == 'yes':
				continue
			else:
				print("Thank you for using Brent's Bank service. Goodbye. ")
				break
				
		elif input_action == 3:
			print(acct_dict[input_account].getBalance())
			repeat_select = str(input("\nWould you like to make another transaction? "))
			if repeat_select.lower() == 'yes':
				continue
			else:
				print("Thank you for using Brent's Bank service. Goodbye. ")
				break
				
		elif input_action == 4:
			print("Thank you for using Brent's Bank service. Goodbye. ")
			break
		break
		
	except:
		print("You did not enter anything.")
	
		

