
from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "18_missing_number.py"

spec = importlib.util.spec_from_file_location(
    "missing_number", program_file
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.find_missing_number([1, 2, 4, 5], 5) == 3
assert module.find_missing_number([1, 3, 4, 5], 5) == 2
assert module.find_missing_number([2, 3, 4, 5], 5) == 1
assert module.find_missing_number([1, 2, 3, 4], 5) == 5
assert module.find_missing_number([1], 2) == 2
assert module.find_missing_number([], 1) == 1
assert module.find_missing_number([1, 2, 3, 5, 6], 6) == 4

print("All test cases passed.")
