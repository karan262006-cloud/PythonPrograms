from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "13_palindrome_string.py"

spec = importlib.util.spec_from_file_location(
    "palindrome_string", program_file
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.is_palindrome_string("madam") == True
assert module.is_palindrome_string("level") == True
assert module.is_palindrome_string("hello") == False
assert module.is_palindrome_string("A") == True
assert module.is_palindrome_string("") == True
assert module.is_palindrome_string("Madam") == True
assert module.is_palindrome_string("python") == False

print("All test cases passed.")
