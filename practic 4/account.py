class Account:
    def __init__ (self,number, owner, balance=0):
        if balance < 0: raise ValueError("недостаточно средств")
        self.number = number
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        if (amount > 0):
            self.balance += amount
        else:
            raise (ValueError("сумма должна быть положительной"))

    def withdraw(self, amount):
        if amount <= 0 :
            raise ValueError("сумма должна быть положительной")
        if ((self.balance - amount) >= 0):
            self.balance -= amount
        else:
            raise (ValueError("недостаточно средств"))

    def __repr__(self):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"
