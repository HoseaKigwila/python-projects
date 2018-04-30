class BankAccount:
    def __init__(self,account_type, amount):
        self.account_type = account_type
        self.amount = amount

    def deposit(self,deposit_amount):
        self.amount += deposit_amount

    def withdraw(self,withdraw_amount):
        self.amount -= withdraw_amount


    def __str__(self):
        return "{} Amount: {}".format(self.account_type,self.amount)


hosea = BankAccount ("checking", 100)
print(hosea.account_type)
print(hosea.amount)

hosea.deposit(30)
print(hosea.amount)

hosea.withdraw(45)
print(hosea.amount)
print (hosea)
