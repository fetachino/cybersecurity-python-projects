# Cybersecurity Python Projects

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![Tests](https://img.shields.io/badge/Tests-unittest-passing-2A9D8F)](#substitution-cipher)
[![Purpose](https://img.shields.io/badge/Purpose-educational_security-6C5CE7)](#substitution-cipher)

Small, tested Python projects that explain security concepts through code.

## Substitution cipher

A command-line monoalphabetic substitution cipher with reusable encode/decode functions, input validation, and automated tests.

![Substitution cipher command-line session](docs/images/substitution-cipher-cli.png)

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

## About the author

Built by **Ahmed Balde** as part of a broader cybersecurity and Python engineering portfolio. See more work on [GitHub](https://github.com/fetachino).
