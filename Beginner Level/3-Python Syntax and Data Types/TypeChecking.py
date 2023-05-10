"""
In this section of code, the isinstance() function is used to check the 
data type of each variable (x, y, z, and a) against the specified data type 
(int, float, str, and bool).

The isinstance() function takes two arguments: the first is the variable 
or value being checked, and the second is the data type being checked against. 
It returns True if the variable or value is of the specified data type, and False otherwise.

For example, isinstance(x, int) returns True because x is an integer, 
while isinstance(y, float) returns True because y is a floating-point number. 
Similarly, isinstance(z, str) returns True because z is a string, 
and isinstance(a, bool) returns True because a is a boolean value.

Type checking is a useful technique in Python programming to ensure that 
variables are of the correct data type before performing operations on them. 
It helps to prevent errors and ensure the correctness of the program.
"""

x = 42
y = 3.14
z = "Hello, world!"
a = True # Define a variable "a" and assign it the boolean value True



# Type checking
print(isinstance(x, int))
print(isinstance(y, float))
print(isinstance(z, int))
print(isinstance(a, bool))