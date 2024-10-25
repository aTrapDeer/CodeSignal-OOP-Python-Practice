# Integer Container Practice Task

Welcome to the Integer Container Practice Task! This repository contains a task designed to help you practice implementing basic operations on a container of integer numbers. The task is divided into several levels, each adding new functionality to the container. You will implement and test your solutions as you progress through the levels.

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [Setup and Installation](#setup-and-installation)
3. [Usage](#usage)
   - [Running Tests](#running-tests)
   - [Project Structure](#project-structure)
4. [Level Specifications](#level-specifications)
   - [Level 1: Adding and Removing Numbers](#level-1-adding-and-removing-numbers)
   - [Level 2: Calculating the Median](#level-2-calculating-the-median)
5. [Example](#example)
6. [Contributing](#contributing)
7. [License](#license)

---

## Project Overview

The Integer Container task challenges you to implement a container that holds integer numbers. As you solve the task, you will add features to the container, progressing through different levels of functionality. The container starts with basic add/remove operations and then evolves to include more complex operations like calculating the median of the numbers in the container.

The project includes pre-implemented test cases to guide and verify your progress. The goal is to pass all tests for each level before moving on to the next.

---

## Setup and Installation

### Clone the Repository:

```bash
git clone <repository-url>
cd integer-container-practice
```

### Install Dependencies:

If you're using a virtual environment, activate it first. Then, install any required dependencies:

```bash
pip install timeout-decorator
```

*Note: This project uses Python's built-in `unittest` framework.*

---

## Usage

### Running Tests

You can run the tests for each level using the provided shell script `run_tests.sh`. Simply specify which level's tests to run. 

To run the tests for **Level 1**:

```bash
./run_tests.sh level_1
```

To run the tests for **Level 2**:

```bash
./run_tests.sh level_2
```

The script will indicate if all tests pass or if there are any failures.

### Project Structure

```bash
integer-container-practice/
├── integer_container.py          # Abstract base class defining the interface for the container.
├── integer_container_impl.py     # Your implementation of the integer container.
├── tests/
│   ├── level_1_tests.py          # Test cases for Level 1 (basic add/remove).
│   ├── level_2_tests.py          # Test cases for Level 2 (calculating the median).
│   └── sandbox_tests.py          # Editable tests for sandbox purposes (not graded).
├── run_tests.sh                  # Script to run the tests.
└── README.md                     # This README file.
```

---

## Level Specifications

### Level 1: Adding and Removing Numbers

- **`add(self, value: int) -> int`**: Adds the specified integer `value` to the container and returns the number of integers in the container after the addition.
  
- **`delete(self, value: int) -> bool`**: Removes the specified integer `value` from the container if it exists. Returns `True` if the value was present and removed, or `False` if the value was not in the container.

### Level 2: Calculating the Median

- **`get_median(self) -> int | None`**: Returns the median integer in the container. If the container is empty, it returns `None`. If the number of elements is even, return the leftmost integer from the two middle integers after sorting.

---

## Example

Here is an example of how the container behaves at different stages:

1. **Adding numbers**:
   - `add(5)` -> Container state: `[5]`
   - `add(10)` -> Container state: `[5, 10]`
   - `add(1)` -> Container state: `[1, 5, 10]`

2. **Calculating the median**:
   - `get_median()` -> Returns `5` (middle value in `[1, 5, 10]`)

3. **Adding more numbers**:
   - `add(4)` -> Container state: `[1, 4, 5, 10]`

4. **Calculating the median again**:
   - `get_median()` -> Returns `4` (leftmost of the two middle values in `[1, 4, 5, 10]`)

5. **Removing numbers**:
   - `delete(1)` -> Container state: `[4, 5, 10]`
   - `get_median()` -> Returns `5`

---

## Contributing

If you wish to contribute by adding more levels or improving the existing code, feel free to submit a pull request.

Steps for contributing:
1. Fork the repository.
2. Create a new branch.
3. Make your changes and submit a pull request with a description of your changes.

---

## License

This project is open-source and available under the MIT License.

