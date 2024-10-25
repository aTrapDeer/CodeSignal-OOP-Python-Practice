# tests/level_3_tests.py

import unittest
from bank_account import BankAccountImpl

class Level3Tests(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.bank_account = BankAccountImpl()

    def test_apply_interest(self):
        self.bank_account.create_account("12345", "savings")
        self.bank_account.deposit("12345", 1000)
        self.bank_account.apply_interest()
        self.assertEqual(self.bank_account.get_balance("12345"), 1050)  # Assume 5% interest

    def test_different_account_types(self):
        self.bank_account.create_account("12345", "savings")
        self.bank_account.create_account("67890", "checking")
        self.bank_account.deposit("12345", 1000)
        self.bank_account.deposit("67890", 2000)
        self.bank_account.apply_interest()  # Interest applied only to savings
        self.assertEqual(self.bank_account.get_balance("12345"), 1050)  # Savings with 5% interest
        self.assertEqual(self.bank_account.get_balance("67890"), 2000)  # No interest for checking

if __name__ == '__main__':
    unittest.main()
