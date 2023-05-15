import re

def is_palindrome(s):
    # Remove spaces and punctuation marks
    s = re.sub(r"[^a-zA-Z0-9]", "", s)
    # Convert to lowercase
    s = s.lower()
    # Check if the string is equal to its reverse
    return s == s[::-1]

# Ask the user to enter a string
user_input = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(user_input):
    print(f'"{user_input}" is a palindrome.')
else:
    print(f'"{user_input}" is not a palindrome.')
