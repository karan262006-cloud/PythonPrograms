from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "16_remove_duplicates.py"

spec = importlib.util.spec_from_file_location(
    "remove_duplicates", program_file
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.remove_duplicates([1, 2, 2, 3, 1, 4]) == [1, 2, 3, 4]
assert module.remove_duplicates([5, 5, 5]) == [5]
assert module.remove_duplicates([]) == []
assert module.remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert module.remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]
assert module.remove_duplicates([0, 0, 1, 0]) == [0, 1]
assert module.remove_duplicates([-1, -1, 2, 2]) == [-1, 2]

print("All test cases passed.")
