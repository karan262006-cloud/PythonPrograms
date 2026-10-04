import sys
import os
import importlib

# Tell Python to look in the current folder for our code
sys.path.append(os.getcwd())

# Load our code file dynamically
largest_module = importlib.import_module("Code.02_largest_of_three")

# Test cases using assert
assert largest_module.find_largest(1, 5, 3) == 5, "Test Failed: 5 should be the largest"
assert largest_module.find_largest(10, 2, 4) == 10, "Test Failed: 10 should be the largest"
assert largest_module.find_largest(-1, -5, 0) == 0, "Test Failed: 0 should be the largest"

print("All test cases passed.")
