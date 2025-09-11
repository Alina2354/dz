class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be a number")
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount

    def get_balance(self) -> float:
        return self.balance

    def __str__(self) -> str:
        return f"Account(owner='{self.owner}', balance={self.balance})"


if __name__ == '__main__':
    account = BankAccount("Alice", 100.0)
    print(account)

    account.deposit(50.0)
    print(f"Баланс после пополнения: {account.get_balance()}")

    account.withdraw(75.0)
    print(f"Баланс после снятия: {account.get_balance()}")

