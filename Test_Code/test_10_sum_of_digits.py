from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "10_sum_of_digits.py"

spec = importlib.util.spec_from_file_location("sum_of_digits", program_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.sum_of_digits(1234) == 10
assert module.sum_of_digits(555) == 15
assert module.sum_of_digits(100) == 1
assert module.sum_of_digits(0) == 0
assert module.sum_of_digits(9) == 9
assert module.sum_of_digits(-123) == 6
assert module.sum_of_digits(9876) == 30

print("All test cases passed.")
