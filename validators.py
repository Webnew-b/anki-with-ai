import re


def validate_word(word: str):
    if not re.fullmatch(r"[A-Za-z]+", word):
        raise ValueError("Input must contain only English letters (A-Z, a-z).")
