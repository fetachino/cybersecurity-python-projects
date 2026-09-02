# Cybersecurity Python Projects

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-unittest-passing-2A9D8F)](#substitution-cipher)
[![Purpose](https://img.shields.io/badge/Purpose-educational_security-6C5CE7)](#substitution-cipher)

Small, tested Python projects that explain security concepts through code.

## Program flow

```mermaid
flowchart LR
    A["User selects an operation"] --> B{"Encode or decode"}
    B -->|Encode| C["Apply substitution mapping"]
    B -->|Decode| D["Apply inverse mapping"]
    C --> E["Preserve case and punctuation"]
    D --> E
    E --> F["Display transformed message"]
    G["Unit tests"] --> C
    G --> D
```

## Substitution cipher

A command-line monoalphabetic substitution cipher with reusable encode/decode functions, input validation, and automated tests.

![Substitution cipher command-line session](docs/images/substitution-cipher-cli.png)

### Encode and decode verification

![Substitution cipher decoding a message back to its original text](docs/images/substitution-cipher-decode.png)

The two CLI captures demonstrate both transformation directions while preserving capitalization, spaces, numbers, and punctuation.

Run it with:

```console
python substitution-cipher/substitution_cipher.py
python -m unittest discover -s tests -v
```

Concepts demonstrated:

- Reversible character transformations
- Separation of reusable logic from the command-line interface
- Input validation and unit testing
- Why classical substitution is unsuitable for real security

> This is an educational cryptography exercise, not secure encryption.

## Verification

The test suite checks a known encoding, reversible round trips, preservation of case and punctuation, and rejection of invalid substitution keys.

Run the test suite with `python -m unittest discover -s tests -v` to verify the reversible transformation and input validation behavior.

Run the test suite with `python -m unittest discover -s tests -v` to verify the reversible transformation and input validation behavior.

## About the author

Built by **Ahmed Balde** as part of a broader cybersecurity and Python engineering portfolio. See more work on [GitHub](https://github.com/fetachino).
