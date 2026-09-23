# Day 13 - Anagram Checker
# Hashing & Lookup

# Take two strings from the user
string1 = input("Enter first string: ").lower().replace(" ", "")
string2 = input("Enter second string: ").lower().replace(" ", "")

# -----------------------------
# Hashmap / Dictionary Approach
# -----------------------------

frequency1 = {}
frequency2 = {}

# Count characters in first string
for char in string1:
    if char in frequency1:
        frequency1[char] += 1
    else:
        frequency1[char] = 1

# Count characters in second string
for char in string2:
    if char in frequency2:
        frequency2[char] += 1
    else:
        frequency2[char] = 1

# Compare dictionaries
if frequency1 == frequency2:
    print("\nResult: The strings are anagrams.")
else:
    print("\nResult: The strings are not anagrams.")

# Display frequency maps
print("\nFirst string frequency:", frequency1)
print("Second string frequency:", frequency2)