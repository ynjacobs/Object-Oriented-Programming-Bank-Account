class BankAccount:



    def __init__(self, balance, interest_rate):
         self.balance = balance
         self.interest_rate = interest_rate

    def __str__(self):
        return "your balance is {} and the interest rate is {}".format(self.balance, self.interest_rate)

    def deposit(self, amount):
        self.balance += amount 
        return self.balance

    def withdraw(self, amount):
        self.balance -= amount 
        return self.balance

    def gain_interest(self):
        self.balance = (( self.interest_rate / 100 ) * self.balance) + self.balance
        return self.balance




my_account = BankAccount( 80000, 1.1)
print(my_account.balance)
my_account = BankAccount( 180000, 1.1)
print(my_account.balance)
my_account = BankAccount( 280000, 1.1)

print(my_account.balance)
# my_account.deposit(3)
new_balance = my_account.deposit(3)
print(new_balance)
new_balance = my_account.withdraw(4)
print(new_balance)
new_balance = my_account.gain_interest()
print(new_balance)

my_other_account = BankAccount(45000, 1.2)
balance = my_other_account.deposit(100)
print(balance, my_other_account)
my_other_account.withdraw(300)
print(balance, my_other_account)
my_other_account.gain_interest()
print(balance, my_other_account)




