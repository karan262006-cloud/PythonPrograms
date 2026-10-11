
from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "04_factorial.py"

spec = importlib.util.spec_from_file_location("factorial_program", program_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.factorial(0) == 1
assert module.factorial(1) == 1
assert module.factorial(5) == 120
assert module.factorial(3) == 6
assert module.factorial(7) == 5040
assert module.factorial(-2) == "Invalid"

print("All test cases passed.")
