class Account:
    def __init__ (self,number, owner, balance=0):
        if balance < 0: raise ValueError("недостаточно средств")
        self.number = number
        self.owner = owner
        self._balance = balance
    def deposit(self, amount):
        if (amount > 0):
            self._balance += amount
        else:
            raise (ValueError("сумма должна быть положительной"))

    @property
    def balance(self):
        return self._balance

    def withdraw(self, amount):
        if amount <= 0 :
            raise ValueError("сумма должна быть положительной")
        if ((self._balance - amount) >= 0):
            self._balance -= amount
        else:
            raise (ValueError("недостаточно средств"))

    def __repr__(self):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"

class SavingsAccount (Account):
    def __init__ (self,number, owner, balance = 0, rate = 0.05 ):
        super().__init__ (number, owner, balance)
        self.rate = rate

    def add_interest(self):
        self._balance = self._balance + self._balance * self.rate

    def __repr__(self):
        return (f"SavingsAccount('{self.number}', '{self.owner}', {self.balance}, {self.rate})")



class CheckingAccount (Account):
    def __init__(self, number, owner, balance=0, overdraft=0):
        super().__init__(number, owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0 :
            raise ValueError("сумма должна быть положительной")
        if self.balance - amount >=  - self.overdraft:
            self._balance -= amount
        else:
            raise ValueError("казна не потянет")

    def __repr__(self):
        return (f"CheckingAccount('{self.number}', '{self.owner}', {self.balance}, {self.overdraft})")
