
from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "03_pos_neg_zero.py"

spec = importlib.util.spec_from_file_location("pos_neg_zero", program_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.check_number(5) == "Positive"
assert module.check_number(-3) == "Negative"
assert module.check_number(0) == "Zero"
assert module.check_number(100) == "Positive"
assert module.check_number(-99) == "Negative"

print("All test cases passed.")
