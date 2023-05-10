# Comparisons Logical and Bitwise operators

x = 42
y = 3.14
z = "Hello, world!"
a = True # Define a variable "a" and assign it the boolean value True


# Comparisons
print(x > y) # Is x greater than y?
print(x < y) # Is x less than y?
print(x == y) # Is x equal to y?
print(x != y) # Is x not equal to y?

# Logical operators
print(a and x > y) # Is a true AND is x greater than y?
print(a or x > y) # Is a true OR is x greater than y?
print(not a) # Is a NOT true?

# Bitwise operators
print(x and y) # Bitwise AND of x and y
print(x or y) # Bitwise OR of x and y

"""

The output of print(x and y) is 3.14 and the output of print(x or y) is 42.

The reason for this is that and and or are bitwise operators 
that work with binary values, but in Python, they are also used as 
logical operators with non-boolean operands.

In the case of x and y, Python evaluates the truthiness of x, 
which is True because it is not zero, empty, or None. Then, 
it evaluates the truthiness of y, which is also True for the same reason. 
Since both operands are True, Python returns the second operand, 
which is y and has a value of 3.14.

In the case of x or y, Python evaluates the truthiness of x first, 
which is True as explained above. Since the first operand is True, 
Python returns it without evaluating the second operand. Therefore, 
the output is x, which has a value of 42.
"""



