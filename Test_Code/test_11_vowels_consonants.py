
from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "11_vowels_consonants.py"

spec = importlib.util.spec_from_file_location(
    "vowels_consonants", program_file
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.count_vowels_consonants("hello") == (2, 3)
assert module.count_vowels_consonants("AEIOU") == (5, 0)
assert module.count_vowels_consonants("xyz") == (0, 3)
assert module.count_vowels_consonants("Python 123!") == (1, 5)
assert module.count_vowels_consonants("") == (0, 0)
assert module.count_vowels_consonants("a b c") == (1, 2)
assert module.count_vowels_consonants("OpenAI") == (4, 2)

print("All test cases passed.")
