class BankAccount:
    def __init__(self,name,balance=0):
        self.account_holder=name
        self.balance=balance

    def deposit(self,amount):
        self.balance=self.balance + amount
        print (f"Deposited : {amount} to your account")

    def withdraw(self,amount):
        if amount>self.balance:
            print("Not Enough Balance !!")
        else:
            print(f"Withdrawn {amount} from {self.balance}")
            self.balance=self.balance-amount

    def __str__(self):
        return f"Account Holder Name: {self.account_holder} \nBalance : {self.balance}"

obj=BankAccount("Dhinakar",100)
print(obj)
# print("\n")

obj.deposit(1000)
print(obj)
# print("\n")

obj.withdraw(500)
print(obj)