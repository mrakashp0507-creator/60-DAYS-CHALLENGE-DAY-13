# 🐍 Day 13 – Anagram Checker

## 📌 Overview

Day 13 focuses on hashing and efficient lookup using Python dictionaries.

The project checks whether two strings are anagrams by counting the frequency of each character.

## 🎯 Problem Statement

Given two strings, determine whether they contain the same characters with the same frequencies.

Example:

listen
silent

Both strings contain the same characters, so they are anagrams.

## 💡 Example

Input:

listen
silent

Output:

The strings are anagrams.

Another example:

hello
world

Output:

The strings are not anagrams.

## 🧠 Hashmap Approach

The program uses Python dictionaries as hashmaps.

Each character is stored as a key and its frequency is stored as the value.

Example:

listen

becomes:

{
    'l': 1,
    'i': 1,
    's': 1,
    't': 1,
    'e': 1,
    'n': 1
}

The frequency maps of both strings are then compared.

## ⚖️ Brute Force vs Hashmap

### Brute Force

One common approach is to sort both strings and compare them.

Example:

listen → eilnst
silent → eilnst

Sorting:

O(n log n)

### Hashmap

The hashmap approach counts each character using a dictionary.

Time Complexity:

O(n)

Space Complexity:

O(k)

where k is the number of unique characters.

## 🌍 Real-World Applications

Hashing and lookup techniques are widely used in software systems.

### Databases

Hash-based indexes can help locate records efficiently.

### Caching

Hashmaps can associate keys with cached values for fast retrieval.

### Authentication

Systems can use lookup structures for managing user-related information.

### Search and Text Processing

Character and word frequency maps can be used to analyze and process text.

## 🛠️ Technologies

- Python 3
- VS Code
- Git
- GitHub

## 📂 Project Structure

Day13-Anagram/
│
├── day13_anagram.py
└── README.md

## 🚀 How to Run

Open the project in VS Code.

Run:

python day13_anagram.py

Example:

Enter first string: listen
Enter second string: silent

Output:

Result: The strings are anagrams.

## 📤 GitHub Submission

git add day13_anagram.py README.md

git commit -m "Complete Day 13 anagram hashing"

git push

## 👨‍💻 Author

Akash

---

🐍 Python Mastery Sprint – Day 13
