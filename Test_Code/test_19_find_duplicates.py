
from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "19_find_duplicates.py"

spec = importlib.util.spec_from_file_location(
    "find_duplicates", program_file
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.find_duplicates([1, 2, 3, 2, 4, 1]) == [2, 1]
assert module.find_duplicates([5, 5, 5]) == [5]
assert module.find_duplicates([1, 2, 3]) == []
assert module.find_duplicates([]) == []
assert module.find_duplicates([1, 1, 2, 2, 3, 3]) == [1, 2, 3]
assert module.find_duplicates([0, 1, 0, 2, 1]) == [0, 1]
assert module.find_duplicates([-1, -2, -1, -2]) == [-1, -2]

print("All test cases passed.")
