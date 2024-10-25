# Bank Account System

This project is a mock **Bank Account System** designed to help you practice object-oriented programming and unit testing. The system progressively adds features over three levels, with each level introducing more complexity. The project follows a structure similar to coding assessments like CodeSignal.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Installation](#installation)
3. [Usage](#usage)
   - [Running Tests](#running-tests)
   - [Project Levels](#project-levels)
4. [Structure](#structure)
5. [Example Commands](#example-commands)

---

## Project Overview

The Bank Account System allows users to create accounts, perform transactions, check balances, and handle different types of accounts (like savings and checking accounts). Each level of the project introduces new features:

- **Level 1**: Implement basic account creation, deposit, and withdrawal.
- **Level 2**: Add functionality for checking account balances and transaction history.
- **Level 3**: Add interest calculation and support for different account types (e.g., savings, checking).

## Installation

To set up the project on your local machine, follow these steps:

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   ```

2. **Navigate to the project directory**:
   ```bash
   cd BankAccountSystem
   ```

3. **(Optional) Set up a virtual environment**:
   It's a good idea to use a virtual environment to manage dependencies. To set it up, run:
   ```bash
   python -m venv venv
   source venv/bin/activate   # For macOS/Linux
   venv\Scripts\activate      # For Windows
   ```

4. **Install dependencies** (if any). This project uses the built-in `unittest` framework, so there are no additional dependencies.

## Usage

### Running Tests

This project uses the **unittest** framework to test the implementation of the bank account system. You can run the tests for each level by using the provided shell script `run_tests.sh`.

To run the tests for each level, use:

```bash
./run_tests.sh level_1   # Run tests for Level 1
./run_tests.sh level_2   # Run tests for Level 2
./run_tests.sh level_3   # Run tests for Level 3
```

The script will tell you whether your implementation is **CORRECT** or **INCORRECT** based on whether all tests pass or fail.

### Project Levels

#### Level 1: Basic Account Operations

- **create_account(account_number: str, account_type: str)**: Creates a new account with the given account number and type (e.g., savings or checking).
- **deposit(account_number: str, amount: float) -> bool**: Deposits the specified amount into the account. Returns `True` if successful.
- **withdraw(account_number: str, amount: float) -> bool**: Withdraws the specified amount from the account if there are sufficient funds. Returns `True` if successful and `False` if there are insufficient funds.

#### Level 2: Checking Balance and Transaction History

- **get_balance(account_number: str) -> float**: Returns the current balance of the account.
- **get_transaction_history(account_number: str) -> list**: Returns a list of all transactions (deposits and withdrawals) for the account.

#### Level 3: Interest Application and Account Types

- **apply_interest()**: Applies interest to all applicable accounts (e.g., savings accounts). Assume a 5% interest rate.
- **Different Account Types**: Supports savings and checking accounts, where interest is only applied to savings accounts.

## Structure

The project directory is structured as follows:

```
BankAccountSystem/
├── bank_account.py              # Core implementation (abstract class + implementation)
├── run_tests.sh                 # Shell script to run tests
├── tests/
│   ├── level_1_tests.py         # Tests for Level 1
│   ├── level_2_tests.py         # Tests for Level 2
│   ├── level_3_tests.py         # Tests for Level 3
├── README.md                    # Project documentation (this file)
```

## Example Commands

To run Level 1 tests:

```bash
./run_tests.sh level_1
```

To run Level 2 tests:

```bash
./run_tests.sh level_2
```

To run Level 3 tests:

```bash
./run_tests.sh level_3
```

## Additional Notes

- You can modify `bank_account.py` to implement the methods defined in each level.
- Each level has corresponding unit tests that validate the correctness of your implementation.
- The shell script `run_tests.sh` will automatically run the tests and tell you whether the solution is correct.

---
