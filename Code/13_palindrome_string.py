def is_palindrome_string(text):
    text = text.lower()
    return text == text[::-1]
