from abc import ABC, abstractmethod

class BankAccount(ABC):
    """
    Abstract class for Bank Account
    """

    @abstractmethod
    def create_account(self, account_number: str, account_type: str):
        """
        Create a new bank account with the given account number and type.
        """
        pass

    @abstractmethod
    def deposit(self, account_number: str, amount: float) -> bool:
        """
        Deposit the specified amount into the account.
        """
        pass

    @abstractmethod
    def withdraw(self, account_number: str, amount: float) -> bool:
        """
        Withdraw the specified amount from the account.
        """
        pass

    @abstractmethod
    def get_balance(self, account_number: str) -> float:
        """
        Return the current balance of the account.
        """
        pass

    @abstractmethod
    def get_transaction_history(self, account_number: str) -> list:
        """
        Return a list of all transactions for the account.
        """
        pass

    @abstractmethod
    def apply_interest(self):
        """
        Apply interest to all applicable accounts.
        """
        pass


class BankAccountImpl(BankAccount):
    def __init__(self):
        self.accounts = {}
        pass

    def create_account(self, account_number: str, account_type: str):
        self.accounts[account_number] = {"account_type": account_type, "balance": 0.0, "transactions": []}
        return len(self.accounts)

    def deposit(self, account_number: str, amount: float) -> bool:
        #Return True if successful, not sure which cases would be flase so I'm just returning true
        # Check if account number exists
        if account_number not in self.accounts:
            print("Account does not exist")
            return False
        print("Depositing")
        print(f"Depositing {amount} into account {account_number}")
        print(f"Current Balance: {self.accounts[account_number]['balance']}")
        # Need to handle float variables
        self.accounts[account_number]["balance"] += amount
        print("Deposit successful")
        print(f"New Balance: {self.accounts[account_number]['balance']}")
        # recording the deposit
        self.accounts[account_number]['transactions'].append({"type": "deposit", "amount": amount})
        return True

    def withdraw(self, account_number: str, amount: float) -> bool:
        #Now if the withdrawal is greater than the balance, return false
        if account_number not in self.accounts:
            print("Account does not exist")
            return False
        if self.accounts[account_number]["balance"]>=amount:
            self.accounts[account_number]["balance"] -= amount
            print(f"Withdrawn {amount} from account {account_number}")
            print(f"New Balance: {self.accounts[account_number]['balance']}")
            # Record the withdraw
            self.accounts[account_number]['transactions'].append({"type": "withdraw", "amount": amount})            
            return True
        else:
            print(f"Attempting to withdraw {amount} from account {account_number} with balance of {self.accounts[account_number]['balance']}")
            print("Insufficient funds")
            return False

    def get_balance(self, account_number: str) -> float:
        if account_number not in self.accounts:
            print("Account does not exist")
            return 0
        print("Looking up balance...")
        return self.accounts[account_number]['balance']

    def get_transaction_history(self, account_number: str) -> list:
        if account_number not in self.accounts:
            print("Account does not exist")
            return []
        print("Looking up transaction history...")
        # had to adjust all the previous to make it work since we build upon it from level 1 to level 2
        return self.accounts[account_number]['transactions']


    def apply_interest(self):
        # For loop through all saving accounts applying a 1.05 multipled by the balance for interest accounting
        for account_number, account_info in self.accounts.items():
            if account_info['account_type'] == 'savings':
                print(f"Account balance pre interest {self.accounts[account_number]['balance']}")
                self.accounts[account_number]['balance'] *= 1.05
                print(f"Interest applied to account {account_number}")
                print(f"New Balance: {self.accounts[account_number]['balance']}")
        pass
