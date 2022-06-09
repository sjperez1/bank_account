# All classes should be capitalized
class Bank_Account:
    # whatever is put here is a global variable
    all_bank_accounts = []
    # classmethod is used when you are accessing something global (directly under class), whereas you can use regular def if it is not something global
    # the following __init__ are attributes specific to certain accounts.
    # when it says that the interest reate should be provided upon instantiation, it means that we should not have a default variable for it and it should be specified when creating an account.
    def __init__(self, int_rate, balance = 0): 
        # instance attributes go here
        self.int_rate = int_rate
        self.balance = balance
        Bank_Account.all_bank_accounts.append(self)
    def deposit(self, amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        self.balance -= amount
        return self
    def display_account_info(self):
        print(f"Balance: ${self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance + (self.balance * self.int_rate)
            return self
    @classmethod
    def all_bank_account_balances(cls):
        for each_account in cls.all_bank_accounts:
            each_balance = each_account.balance
            print(f"Balance: ${each_balance}")
        # Chain methods of an instance (not a class), so nothing similar to return self is needed. In addition, the goal is just to print here.
        
account1 = Bank_Account(0.045, 200)
account2 = Bank_Account(0.04, 650)

# for the methods where there is nothing in parentheses, we are only passing in the self value.
account1.deposit(433).deposit(153).deposit(48).withdraw(198).yield_interest().display_account_info()
account2.deposit(212).deposit(119).withdraw(13).withdraw(22).withdraw(29).withdraw(46).yield_interest().display_account_info()

Bank_Account.all_bank_account_balances()