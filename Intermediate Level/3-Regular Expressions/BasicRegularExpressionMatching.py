import re

# search for the pattern 'apple' in the given string
string = 'I like apples and oranges'
match = re.search('apple', string)

# check if the match was found
if match:
    print('Match found:', match.group())
else:
    print('Match not found')


"""
In this example, we use the re module to search for the pattern 'apple' in the given string. 
We use the search() method to perform the search and it returns a match object. 
We check if the match was found using an if-else statement and print the match 
if it was found.
"""