import re

# extract all the email addresses from a given string
string = 'Please contact me at john@example.com or jane@example.com'
matches = re.findall(r'[\w\.-]+@[\w\.-]+', string)

# print the list of email addresses
print(matches)


'''
In this example, we use a regular expression to extract all the email addresses from a 
given string. The regular expression [\w\.-]+@[\w\.-]+ matches one or 
more word characters (\w), dots (.), or dashes (-) before the @ symbol, 
followed by one or more word characters, dots, or dashes after the @ symbol.

We use the findall() method to find all the matches in the string and it 
returns a list of matches. We then print the list of email addresses.
'''