import unittest
from dz39 import BankAccount

class TestBankAccount(unittest.TestCase):
    def test_deposit(self):
        account = BankAccount("Alice", 100.0)
        self.assertEqual(str(account), "Account(owner='Alice', balance=100.0)")

    def test_deposit_positive_amount(self):
        account = BankAccount("Bob", 50.0)
        account.deposit(50.0)
        self.assertEqual(account.get_balance(), 100.0)

    def test_withdraw(self):
        account = BankAccount("Charlie", 200.0)
        account.withdraw(50.0)
        self.assertEqual(account.get_balance(), 150.0)

    def test_withdraw_insufficient_funds(self):
        account = BankAccount("David", 10.0)
        with self.assertRaises(ValueError):
            account.withdraw(50.0)

    def test_get_balance(self):
        account = BankAccount("Frank", 75.50)
        self.assertEqual(account.get_balance(), 75.50)


if __name__ == '__main__':
    unittest.main()

