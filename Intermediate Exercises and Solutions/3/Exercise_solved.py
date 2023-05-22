#Exercise 3: Palindrome Checker

'''

Write a Python program that asks the user to enter a string and checks if it is a palindrome.
A palindrome is a word, phrase, number, or other sequence of characters that reads the same 
backward and forward (ignoring spaces, punctuation, and capitalization).
'''


'''
Your program should perform the following steps:
    Ask the user to enter a string.

    Remove all spaces and punctuation marks from the string.

    Convert the string to lowercase.

    Check if the string is equal to its reverse.

    If the string is a palindrome, print a message saying so. Otherwise, 
    print a message saying that the string is not a palindrome.
'''
#Example output:

'''
Enter a string: A man, a plan, a canal: Panama!
"A man a plan a canal Panama" is a palindrome.


'''
import re
str=input("Please enter a string: ")
str_lowercase=str.lower()
str_lowercase_punct_replaced=re.sub(r"""[,.'?!-(){}:;@#&$ ]+\ *""","",str_lowercase)
str_lowercase_punct_replaced_reversed=str_lowercase_punct_replaced[::-1]

if str_lowercase_punct_replaced==str_lowercase_punct_replaced_reversed:
    print("The string is a Palindrome!!")
else:
    print("The string is not a Palindrome")