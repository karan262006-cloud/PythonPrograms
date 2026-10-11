
from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "06_prime_number.py"

spec = importlib.util.spec_from_file_location("prime_program", program_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_prime(2) is True
assert module.is_prime(3) is True
assert module.is_prime(7) is True
assert module.is_prime(9) is False
assert module.is_prime(1) is False
assert module.is_prime(0) is False
assert module.is_prime(-5) is False
assert module.is_prime(97) is True

print("All test cases passed.")
