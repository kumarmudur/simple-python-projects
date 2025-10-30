class Account:
    def __init__(self, id, holder_name):
        self.id = id
        self.holder_name = holder_name
        self._balance = 0  # encapsulation

    def check_balance(self):
        print(f"Balance: {self._balance}")

    def deposit(self, amount):
        self._balance += amount
        print(f"Deposit successful. Updated balance: {self._balance}")

    def withdraw(self, amount):
        if self._balance >= amount:
            self._balance -= amount
            print(f"Withdraw successful. Updated balance: {self._balance}")
        else:
            print("Insufficient funds")


class SavingsAccount(Account):
    def calculate_interest(self):
        INTEREST_RATE = 0.04  # 4%
        interest = self._balance * INTEREST_RATE
        print(f"Interest: {interest}")


class CurrentAccount(Account):
    def withdraw(self, amount):  # polymorphism
        OVER_DRAFT = 1000
        if self._balance + OVER_DRAFT >= amount:
            self._balance -= amount
            print(f"Withdraw successful. Updated balance: {self._balance}")
        else:
            print("Insufficient funds")


class Bank:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.__accounts = {}

    def create_account(self, id, holder_name, type):
        if type == 'savings':
            new_account = SavingsAccount(id, holder_name)
        elif type == 'current':
            new_account = CurrentAccount(id, holder_name)
        self.__accounts[id] = new_account
        print("Account creation successful")
        return new_account

    def get_account(self, id):
        if id not in self.__accounts:
            print("Account not found!")
            return None
        else:
            account = self.__accounts[id]
            print(f"\nID: {account.id}\nHolder name: {account.holder_name}")
            return account


sbk = Bank('Shiva', 'Shivamogga')

s1 = sbk.create_account("1", "Shiva", "savings")
c1 = sbk.create_account("2", "Shankar", "current")


sbk.get_account("1")



