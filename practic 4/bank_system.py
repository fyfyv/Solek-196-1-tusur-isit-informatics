class Account:
    def __init__(self, number, owner, balance=0):
        if balance < 0:
            raise ValueError("начальный остаток не может быть отрицательным")
        self.number = number
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("сумма должна быть положительной")
        self._balance += amount

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("сумма должна быть положительной")
        if self._balance - amount < 0:
            raise ValueError("недостаточно средств")
        self._balance -= amount

    @property
    def balance(self):
        return self._balance

    def __repr__(self):
        return f"Account('{self.number}', '{self.owner}', {self.balance})"


class SavingsAccount(Account):
    def __init__(self, number, owner, balance=0, rate=0.05):
        super().__init__(number, owner, balance)
        self.rate = rate

    def add_interest(self):
        self._balance += self._balance * self.rate

    def __repr__(self):
        return f"SavingsAccount('{self.number}', '{self.owner}', {self.balance}, {self.rate})"


class CheckingAccount(Account):
    def __init__(self, number, owner, balance=0, overdraft=0):
        super().__init__(number, owner, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("сумма должна быть положительной")
        if self._balance - amount < -self.overdraft:
            raise ValueError("превышен овердрафт")
        self._balance -= amount

    def __repr__(self):
        return f"CheckingAccount('{self.number}', '{self.owner}', {self.balance}, {self.overdraft})"


class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id
        self._accounts = []

    def add_account(self, account):
        self._accounts.append(account)

    def remove_account(self, number):
        self._accounts = [a for a in self._accounts if a.number != number]

    def accounts(self):
        return list(self._accounts)

    def total_balance(self):
        return sum(account.balance for account in self._accounts)

    def __repr__(self):
        return f"Customer('{self.name}', '{self.customer_id}')"


class Bank:
    def __init__(self):
        self._customers = {}
        self._accounts = {}
        self._owners = {}

    def add_customer(self, customer):
        if customer.customer_id in self._customers:
            raise ValueError("клиент с таким номером уже есть")
        self._customers[customer.customer_id] = customer

    def customer(self, customer_id):
        return self._customers[customer_id]

    def open_account(self, customer_id, account):
        customer = self.customer(customer_id)
        if account.number in self._accounts:
            raise ValueError("счёт с таким номером уже открыт")
        self._accounts[account.number] = account
        self._owners[account.number] = customer_id
        customer.add_account(account)

    def close_account(self, number):
        account = self._accounts[number]
        if account.balance != 0:
            raise ValueError("нельзя закрыть счёт с ненулевым остатком")
        customer_id = self._owners.pop(number)
        del self._accounts[number]
        self._customers[customer_id].remove_account(number)

    def transfer(self, from_number, to_number, amount):
        if from_number == to_number:
            raise ValueError("нельзя перевести деньги на тот же счёт")
        source = self._accounts[from_number]
        target = self._accounts[to_number]
        source.withdraw(amount)
        target.deposit(amount)

    def accounts(self, customer_id, min_balance=None):
        customer = self.customer(customer_id)
        result = customer.accounts()
        if min_balance is not None:
            result = [a for a in result if a.balance >= min_balance]
        return result

    def total_deposits(self):
        return sum(account.balance for account in self._accounts.values())
