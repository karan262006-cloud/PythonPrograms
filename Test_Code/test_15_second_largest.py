from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "15_second_largest.py"

spec = importlib.util.spec_from_file_location("second_largest", program_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.second_largest([10, 5, 8, 10, 3]) == 8
assert module.second_largest([1, 2, 3, 4, 5]) == 4
assert module.second_largest([10, 10, 9]) == 9
assert module.second_largest([-1, -5, -3]) == -3
assert module.second_largest([7, 7, 7]) is None
assert module.second_largest([5]) is None
assert module.second_largest([]) is None
assert module.second_largest([2, 1]) == 1

print("All test cases passed.")
