# tests/level_2_tests.py

import unittest
from bank_account import BankAccountImpl

class Level2Tests(unittest.TestCase):
    
    @classmethod
    def setUp(cls):
        cls.bank_account = BankAccountImpl()

    def test_balance(self):
        self.bank_account.create_account("12345", "savings")
        self.bank_account.deposit("12345", 1000)
        self.assertEqual(self.bank_account.get_balance("12345"), 1000)

    def test_transaction_history(self):
        self.bank_account.create_account("12345", "savings")
        self.bank_account.deposit("12345", 1000)
        self.bank_account.withdraw("12345", 200)
        self.assertEqual(self.bank_account.get_transaction_history("12345"), [
            {"type": "deposit", "amount": 1000},
            {"type": "withdraw", "amount": 200}
        ])

if __name__ == '__main__':
    unittest.main()
