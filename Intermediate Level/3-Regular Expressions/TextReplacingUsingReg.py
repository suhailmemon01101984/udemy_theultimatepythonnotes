import re

# replace all occurrences of 'apples' with 'oranges' in a given string
string = 'I like apples and applesauce'
new_string = re.sub('apples', 'oranges', string)

# print the new string
print(new_string)


'''
In this example, we use the sub() method to replace all occurrences 
of 'apples' with 'oranges' in a given string. 
The sub() method takes three arguments - the pattern to search for, 
the replacement string, and the original string.
'''