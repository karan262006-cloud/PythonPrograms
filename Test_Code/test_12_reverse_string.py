from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "12_reverse_string.py"

spec = importlib.util.spec_from_file_location("reverse_string", program_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.reverse_string("hello") == "olleh"
assert module.reverse_string("Python") == "nohtyP"
assert module.reverse_string("12345") == "54321"
assert module.reverse_string("a") == "a"
assert module.reverse_string("") == ""
assert module.reverse_string("madam") == "madam"
assert module.reverse_string("Hello World") == "dlroW olleH"

print("All test cases passed.")
