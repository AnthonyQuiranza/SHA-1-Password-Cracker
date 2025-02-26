# SHA-1 Password Cracker

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Project Status](https://img.shields.io/badge/Status-Completed-green.svg)

## Overview

This project is a solution to the **SHA-1 Password Cracker** challenge from freeCodeCamp's Python curriculum. It implements a password cracker that attempts to reverse SHA-1 hashed passwords by comparing them against a list of the top 10,000 most common passwords. The cracker can optionally use a list of known salts to test prepended and appended combinations.

The goal of this project is to demonstrate the importance of strong password hashing and security practices by showing how weaker hashes (like SHA-1) can be vulnerable to cracking attempts.

## Features

- Cracks SHA-1 hashed passwords using a list of top 10,000 common passwords
- Supports optional salt usage (prepend and append) from a known salts list
- Returns the original password if found, or "PASSWORD NOT IN DATABASE" if not
- Includes test cases from the freeCodeCamp challenge
- Built with Python's `hashlib` library
