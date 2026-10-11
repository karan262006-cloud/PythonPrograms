from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "14_char_frequency.py"

spec = importlib.util.spec_from_file_location("char_frequency", program_file)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.char_frequency("hello") == {
    "h": 1, "e": 1, "l": 2, "o": 1
}
assert module.char_frequency("aabbc") == {
    "a": 2, "b": 2, "c": 1
}
assert module.char_frequency("") == {}
assert module.char_frequency("aaa") == {"a": 3}
assert module.char_frequency("Python") == {
    "P": 1, "y": 1, "t": 1, "h": 1, "o": 1, "n": 1
}
assert module.char_frequency("a a") == {
    "a": 2, " ": 1
}
assert module.char_frequency("Hello!") == {
    "H": 1, "e": 1, "l": 2, "o": 1, "!": 1
}

print("All test cases passed.")
