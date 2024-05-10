#!/bin/bash

# Alex Karapetkov
# CS412 NP-Complete Project
    # Traveling Salesman Problem
    # Shell script to run test cases

# Data sets used for some test cases:
# https://www.math.uwaterloo.ca/tsp/world/countries.html
# https://people.sc.fsu.edu/~jburkardt/datasets/tsp/tsp.html


# programs to run test cases on
PROGRAM1="cs412_tsp_approx.py"
PROGRAM2="cs412_tsp_optimal.py"

# list of test case files
TEST_CASES=("test_cases/testcase1" "test_cases/testcase2" "test_cases/testcase3" "test_cases/testcase4"
            "test_cases/testcase5" "test_cases/testcase6" "test_cases/testcase7" "test_cases/testcase8")

# loop over all test cases for program 1
for TEST_CASE in ${TEST_CASES[@]}
do
    echo "Running $PROGRAM1 on $TEST_CASE"
    OUTPUT1=$(mktemp)
    INPUT_FILE="${TEST_CASE}_input.txt"

    # measure the execution time of program 1
    START_TIME=$(date +%s.%N)
    python3 "$PROGRAM1" < "$INPUT_FILE" > "$OUTPUT1"
    END_TIME=$(date +%s.%N)
    EXECUTION_TIME=$(echo "$END_TIME - $START_TIME" | bc)

    echo "Input file contents ($INPUT_FILE):"
    #cat "$INPUT_FILE"
    echo "Program output:"
    cat "$OUTPUT1"
    echo "Execution time: $EXECUTION_TIME seconds"


    if diff -q --strip-trailing-cr "$OUTPUT1" "${TEST_CASE}_output.txt"; then
        echo "$TEST_CASE passed"
    else
        echo "$TEST_CASE failed"
    fi
    rm "$OUTPUT1"

    #loop over all test cases for program 2
    echo "Running $PROGRAM2 on $TEST_CASE"
    OUTPUT2=$(mktemp)

    # measure the execution time of program 2
    START_TIME=$(date +%s.%N)
    python3 "$PROGRAM2" < "$INPUT_FILE" > "$OUTPUT2"
    END_TIME=$(date +%s.%N)
    EXECUTION_TIME2=$(echo "$END_TIME - $START_TIME" | bc)

    echo "Input file contents ($INPUT_FILE):"
    #cat "$INPUT_FILE"
    echo "Program output:"
    cat "$OUTPUT2"
    echo "Execution time: $EXECUTION_TIME seconds"

    if diff -q --strip-trailing-cr "$OUTPUT2" "${TEST_CASE}_output.txt"; then
        echo "$TEST_CASE passed for $PROGRAM2"
    else
        echo "$TEST_CASE failed for $PROGRAM2"
    fi

    rm "$OUTPUT2"
done
