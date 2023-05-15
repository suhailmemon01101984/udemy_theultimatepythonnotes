#Explain Regular Expression

import re

# Example 1: Matching a pattern in a string
string = "The quick brown fox jumps over the lazy dog"
pattern = "quick"
match = re.search(pattern, string)
if match:
    print(f"Found a match: '{match.group(0)}'")
else:
    print("No match found")

# Example 2: Finding all matches in a string
string = "The quick brown fox jumps over the lazy dog"
pattern = "the"
matches = re.findall(pattern, string, re.IGNORECASE)
if matches:
    print(f"Found {len(matches)} matches: {matches}")
else:
    print("No matches found")

# Example 3: Replacing a pattern in a string
string = "The quick brown fox jumps over the lazy dog"
pattern = "brown"
replacement = "red"
new_string = re.sub(pattern, replacement, string)
print(f"Original string: {string}")
print(f"New string: {new_string}")



'''

In Example 1, we demonstrate how to match a pattern in a string using the re.search() function. 
We search for the pattern "quick" in the string "The quick brown fox jumps over the lazy dog". 
If a match is found, we print the matched text using the group() method of the MatchObject returned by re.search().

In Example 2, we show how to find all occurrences of a pattern in a string using the re.findall() function. 
We search for the pattern "the" (ignoring case) in the same string as Example 1. 
If any matches are found, we print the number of matches and the matched text.

In Example 3, we demonstrate how to replace a pattern in a string using the re.sub() function. 
We replace the pattern "brown" with "red" in the string "The quick brown fox jumps over the lazy dog". 
We then print both the original and modified strings to show the replacement in action.

This is just a simple introduction to regular expressions in Python.
'''