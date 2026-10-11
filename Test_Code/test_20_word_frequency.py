from pathlib import Path
import importlib.util

project_folder = Path(__file__).resolve().parents[1]
program_file = project_folder / "Code" / "20_word_frequency.py"

spec = importlib.util.spec_from_file_location(
    "word_frequency", program_file
)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

assert module.word_frequency("python is fun") == {
    "python": 1, "is": 1, "fun": 1
}
assert module.word_frequency("hello hello world") == {
    "hello": 2, "world": 1
}
assert module.word_frequency("") == {}
assert module.word_frequency("Python python PYTHON") == {
    "python": 3
}
assert module.word_frequency("one two one three two one") == {
    "one": 3, "two": 2, "three": 1
}
assert module.word_frequency("a b a") == {
    "a": 2, "b": 1
}
assert module.word_frequency("DevOps is fun and DevOps is useful") == {
    "devops": 2, "is": 2, "fun": 1, "and": 1, "useful": 1
}

print("All test cases passed.")
