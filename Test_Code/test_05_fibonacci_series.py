
from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "05_fibonacci_series.py"

spec = importlib.util.spec_from_file_location("fibonacci_program", program_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.fibonacci_series(0) == []
assert module.fibonacci_series(1) == [0]
assert module.fibonacci_series(2) == [0, 1]
assert module.fibonacci_series(7) == [0, 1, 1, 2, 3, 5, 8]
assert module.fibonacci_series(5) == [0, 1, 1, 2, 3]
assert module.fibonacci_series(-3) == []

print("All test cases passed.")
