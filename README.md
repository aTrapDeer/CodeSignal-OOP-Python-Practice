# CodeSignal OOP Practice Repository

This repository contains practice problems designed to help improve your Object-Oriented Programming (OOP) skills. The problems are structured similarly to CodeSignal tasks, and each task progressively adds complexity through multiple levels.

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup and Installation](#setup-and-installation)
3. [Usage](#usage)
   - [Running Tests](#running-tests)
   - [Project Structure](#project-structure)
4. [Problem Descriptions](#problem-descriptions)
   - [Problem 1: Task Management System](#problem-1-task-management-system)
   - [Problem 2: Bank Account System](#problem-2-bank-account-system)
5. [Contributing](#contributing)
6. [License](#license)

---

## Project Overview

This repository contains multiple problems to help you practice object-oriented design and implementation. Each problem has been broken down into **three levels**, where each level introduces additional features to the existing system. The problems use Python’s built-in `unittest` framework to check for correctness.

---

## Setup and Installation

1. **Clone the repository**:
   ```bash
   git clone <your-repo-url>
   cd CodeSignal-OOP-Practice
   ```

2. **Set up a Python virtual environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/macOS
   venv\Scripts\activate     # For Windows
   ```

3. **Install any dependencies** (if needed):
   No external dependencies are required, as we are using Python’s built-in `unittest` framework.

---

## Usage

### Running Tests

You can run the tests for each level using the provided shell script `run_tests.sh`. To execute the tests for a specific level, use the following command:

```bash
./run_tests.sh <level_number>
```

For example:
- Run **Level 1** tests:
  ```bash
  ./run_tests.sh level_1
  ```

- Run **Level 2** tests:
  ```bash
  ./run_tests.sh level_2
  ```

- Run **Level 3** tests:
  ```bash
  ./run_tests.sh level_3
  ```

The script will inform you if all tests pass or if there are any failures.

### Project Structure

```
CodeSignal-OOP-Practice/
├── task_management/
│   ├── task_manager.py           # Implementation for the Task Management System
│   ├── tests/
│   │   ├── level_1_tests.py      # Level 1 tests for Task Management
│   │   ├── level_2_tests.py      # Level 2 tests for Task Management
│   │   ├── level_3_tests.py      # Level 3 tests for Task Management
│   └── run_tests.sh              # Script to run tests for Task Management System
├── bank_account/
│   ├── bank_account.py           # Implementation for the Bank Account System
│   ├── tests/
│   │   ├── level_1_tests.py      # Level 1 tests for Bank Account System
│   │   ├── level_2_tests.py      # Level 2 tests for Bank Account System
│   │   ├── level_3_tests.py      # Level 3 tests for Bank Account System
│   └── run_tests.sh              # Script to run tests for Bank Account System
└── README.md                     # This README file
```

---

## Problem Descriptions

### Problem 1: Task Management System

#### Level 1: Basic Task Operations
- Implement functionality for adding, deleting, and listing tasks in the system.

#### Level 2: Task Prioritization
- Extend the system to allow tasks to be prioritized and listed by priority.

#### Level 3: Task Categories
- Add support for task categories, and implement functionality to list tasks by category.

#### To run tests for this problem:
```bash
cd task_management
./run_tests.sh <level_number>
```

---

### Problem 2: Bank Account System

#### Level 1: Basic Account Operations
- Implement functionality to create bank accounts, deposit money, and withdraw money.

#### Level 2: Transaction History
- Add support for tracking transaction history (deposits and withdrawals).

#### Level 3: Interest Application and Account Types
- Implement interest calculation for savings accounts and ensure that different account types (savings vs. checking) are handled correctly.

#### To run tests for this problem:
```bash
cd bank_account
./run_tests.sh <level_number>
```

---

## Contributing

If you would like to contribute to this repository by adding more problems, improving existing solutions, or enhancing the test cases, feel free to fork the repo and submit a pull request.

1. Fork the repository.
2. Create a new branch.
3. Make your changes and submit a PR with an appropriate description.

---

## License

This project is open-source and available under the MIT License.
Designed by Andrew Rapier, 2024
---
