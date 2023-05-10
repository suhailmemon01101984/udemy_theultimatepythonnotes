#Variables and Data Types


'''
In Python, variables are used to store values.
To create a variable, you simply choose a name
for the variable and assign a value to it using the equals sign (=).

For example:
'''

x = 5
y = "Hello, World!"


'''
In this example, we've created two variables:
x and y. x is an integer (specifically, the value 5), 
and y is a string (specifically, the message "Hello, World!").


Python has several built-in data types, including:

Integers: Whole numbers, such as 5, -3, and 0.
Floating-point numbers: Numbers with a decimal point, such as 3.14, -2.5, and 0.0.
Strings: Sequences of characters, such as "Hello, World!", "Python is great", and "123".
Booleans: True or False values.

'''

print(type(x))
print(type(y))

# The output will show 
# x= <class 'int'> | Which means that x is integer
# y = <class 'str'> | Which means that y is string


########

# Define a new variable "x" and assign it the integer value 42
x = 42

# Print the value of "x" and its data type to the console
print(x, type(x))

# Define a new variable "y" and assign it the floating-point value 3.14
y = 3.14

# Print the value of "y" and its data type to the console
print(y, type(y))

# Define a variable "z" and assign it the string value "Hello, world!"
z = "Hello, world!"

# Print the value of "z" and its data type to the console
print(z, type(z))

# Define a variable "a" and assign it the boolean value True
a = True

# Print the value of "a" and its data type to the console
print(a, type(a))


"""
The output will show
 
42 <class 'int'>
3.14 <class 'float'>
Hello, world! <class 'str'>
True <class 'bool'>
"""