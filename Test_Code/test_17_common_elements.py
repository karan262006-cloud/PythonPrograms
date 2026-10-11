
from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "17_common_elements.py"

spec = importlib.util.spec_from_file_location(
    "common_elements", program_file
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.common_elements([1, 2, 3, 4], [3, 4, 5, 6]) == [3, 4]
assert module.common_elements([1, 2], [3, 4]) == []
assert module.common_elements([], [1, 2]) == []
assert module.common_elements([1, 1, 2, 3], [1, 2, 2]) == [1, 2]
assert module.common_elements([5, 4, 3], [3, 4, 5]) == [5, 4, 3]
assert module.common_elements([1, 2, 3], [3, 2, 1]) == [1, 2, 3]
assert module.common_elements([-1, 0, 1], [0, 1, 2]) == [0, 1]

print("All test cases passed.")
