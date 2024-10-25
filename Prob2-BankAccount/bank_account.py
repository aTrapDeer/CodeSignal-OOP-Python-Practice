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
        # TODO: Implement your solution here
        pass

    def create_account(self, account_number: str, account_type: str):
        # TODO: Implement account creation
        pass

    def deposit(self, account_number: str, amount: float) -> bool:
        # TODO: Implement deposit functionality
        pass

    def withdraw(self, account_number: str, amount: float) -> bool:
        # TODO: Implement withdrawal functionality
        pass

    def get_balance(self, account_number: str) -> float:
        # TODO: Implement balance check functionality
        pass

    def get_transaction_history(self, account_number: str) -> list:
        # TODO: Implement transaction history functionality
        pass

    def apply_interest(self):
        # TODO: Implement interest application
        pass

