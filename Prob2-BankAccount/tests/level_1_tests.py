# tests/level_1_tests.py

import unittest
from bank_account import BankAccountImpl

class Level1Tests(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.bank_account = BankAccountImpl()

    def test_create_account(self):
        self.bank_account.create_account("12345", "savings")
        self.bank_account.create_account("67890", "checking")

    def test_deposit(self):
        self.bank_account.create_account("12345", "savings")
        self.assertTrue(self.bank_account.deposit("12345", 500))
        self.assertTrue(self.bank_account.deposit("12345", 200))

    def test_withdraw(self):
        self.bank_account.create_account("12345", "savings")
        self.bank_account.deposit("12345", 500)
        self.assertTrue(self.bank_account.withdraw("12345", 200))
        self.assertFalse(self.bank_account.withdraw("12345", 400))  # Balance insufficient

if __name__ == '__main__':
    unittest.main()
