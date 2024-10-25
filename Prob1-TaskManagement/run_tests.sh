#!/bin/bash

# This script runs different levels of tests for the Task Management System.
# Usage: ./run_tests.sh level_1    # To run tests for Level 1
#        ./run_tests.sh level_2    # To run tests for Level 2
#        ./run_tests.sh level_3    # To run tests for Level 3

# Check if a level argument is provided
if [ -z "$1" ]; then
    echo "Error: No test level provided."
    echo "Usage: $0 <level_1|level_2|level_3>"
    exit 1
fi

# Function to run tests and determine correctness
run_tests() {
    python -m unittest discover -s tests -p "$1"  # Run the specific level test file

    # Check the exit code of the last command (unittest)
    if [ $? -eq 0 ]; then
        echo "CORRECT: All tests passed for $1"
    else
        echo "INCORRECT: Some tests failed for $1"
    fi
}

# Determine which level of tests to run based on the argument
if [ "$1" == "level_1" ]; then
    echo "Running Level 1 Tests..."
    run_tests "level_1_tests.py"

elif [ "$1" == "level_2" ]; then
    echo "Running Level 2 Tests..."
    run_tests "level_2_tests.py"

elif [ "$1" == "level_3" ]; then
    echo "Running Level 3 Tests..."
    run_tests "level_3_tests.py"

else
    echo "Error: Invalid test level provided."
    echo "Usage: $0 <level_1|level_2|level_3>"
    exit 1
fi

# Pause the terminal before closing
echo "Press any key to exit..."
read -n 1 -s
