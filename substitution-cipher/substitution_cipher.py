"""Educational monoalphabetic substitution cipher."""

import string

ALPHABET = string.ascii_uppercase
DEFAULT_KEY = "XPMGTDHLYONZBWEARKJUFSCIQV"


def validate_key(key: str) -> str:
    """Return a normalized key or raise ValueError if it is invalid."""
    normalized = key.upper()
    if len(normalized) != len(ALPHABET) or set(normalized) != set(ALPHABET):
        raise ValueError("Key must contain every English letter exactly once.")
    return normalized


def encode(plaintext: str, key: str = DEFAULT_KEY) -> str:
    """Encode text while preserving spaces, punctuation, and letter case."""
    normalized_key = validate_key(key)
    return plaintext.translate(_translation_table(ALPHABET, normalized_key))


def decode(ciphertext: str, key: str = DEFAULT_KEY) -> str:
    """Decode text produced by encode."""
    normalized_key = validate_key(key)
    return ciphertext.translate(_translation_table(normalized_key, ALPHABET))


def _translation_table(source: str, destination: str) -> dict[int, str]:
    return str.maketrans(
        source + source.lower(), destination + destination.lower()
    )


def main() -> None:
    """Run the interactive command-line interface."""
    print("Educational substitution cipher")
    while True:
        choice = input("[E]ncode, [D]ecode, or [Q]uit: ").strip().lower()
        if choice == "q":
            return
        if choice not in {"e", "d"}:
            print("Enter E, D, or Q.")
            continue
        message = input("Message: ")
        transform = encode if choice == "e" else decode
        print(transform(message))


if __name__ == "__main__":
    main()
