from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "08_reverse_number.py"

spec = importlib.util.spec_from_file_location("reverse_number", program_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.reverse_number(1234) == 4321
assert module.reverse_number(567) == 765
assert module.reverse_number(100) == 1
assert module.reverse_number(7) == 7
assert module.reverse_number(0) == 0
assert module.reverse_number(-123) == -321
assert module.reverse_number(1200) == 21

print("All test cases passed.")
