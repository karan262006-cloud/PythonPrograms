import sys
import os
import importlib

# Tell Python to look in the current folder for our code
sys.path.append(os.getcwd())

# Load our code file
even_odd = importlib.import_module("Code.01_even_odd")

# Test cases using assert
assert even_odd.is_even(4) is True, "Test Failed: 4 should be Even"
assert even_odd.is_even(7) is False, "Test Failed: 7 should be Odd"
assert even_odd.is_even(0) is True, "Test Failed: 0 should be Even"

print("All test cases passed.")
