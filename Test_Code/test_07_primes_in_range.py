
from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "07_primes_in_range.py"

spec = importlib.util.spec_from_file_location("primes_range", program_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.primes_in_range(1, 10) == [2, 3, 5, 7]
assert module.primes_in_range(10, 20) == [11, 13, 17, 19]
assert module.primes_in_range(2, 2) == [2]
assert module.primes_in_range(14, 16) == []
assert module.primes_in_range(-5, 5) == [2, 3, 5]
assert module.primes_in_range(20, 10) == []

print("All test cases passed.")
