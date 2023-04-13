import sys
class Customer:
 bank_name="Indian Bank"
 def __init__(self,name,account_number,balance=0):
    self.name=name
    self.balance=balance 
    self.account_number=account_number
 
 def deposit(self,amount):
    self.balance=self.balance+amount
 
    print("Balance After Deposit ",self.balance)
 
 def withdraw(self,amount): 
    if amount>self.balance:
        print("Insufficient balance we cannot process your request")
        sys.exit()
    self.balance=self.balance-amount 
    print("Balance After Withdrawal :",self.balance)
 
 def check_balance(self):
    print("Balance Available :",self.balance)
 
print("Welcome to",Customer.bank_name)
name=input("Please enter your name")
account_number=int(input("Enter Your Account Number"))
print("----------------------------------------------------------------------------------")
print("Customer Name is :", name)
print("Customer Account Number is ",account_number)
print("----------------------------------------------------------------------------------")
    
c=Customer(name,account_number)
while True:
    print("**********************************************************************************************")
    print("Press D -- FOR DEPOSIT MONEY ")
    print("Press W -- FOR WITHDRAWAL MONEY")
    print("Press B -- FOR BALANCE CHECKING")
    print("Press E -- FOR EXIT")
    print("***********************************************************************************************")
    option = input("Choose your Option for Transaction")
    if option == "D" or option =="d":
        amount=int(input("Enter the Amount You want to Deposit"))
        c.deposit(amount)
    elif option == "W" or option =="w":
        amount=int(input("Enter the Amount You want to Withdrawal"))
        c.withdraw(amount)
    elif option == "B" or option == "b":
        c.check_balance()
    elif option == "E" or option == "e":
        print("Thanks for Banking!!!")
        sys.exit()
    else:
        print("Please enter valid input")