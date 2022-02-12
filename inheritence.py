class Account():
    def __init__(self,name,balance,account_number):
        self.name = name
        self.balance = balance
        self.account_number = account_number

class SavingsAccount(Account):
    def __init__(self,name,balance,account_number):
        super().__init__(name,balance,account_number)
        self.interest_rate=3.4

a = Account("Abdullah",12334,97986)
b = SavingsAccount("Ansari",6986,98679)
print(a.name,a.balance,a.account_number)
print(b.name,b.balance,b.account_number)