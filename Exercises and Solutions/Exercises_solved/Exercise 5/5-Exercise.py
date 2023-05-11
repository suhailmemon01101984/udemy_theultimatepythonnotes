# Exercise: Type checking

'''
Write a Python function called check_types that 
takes three arguments, x, y, and z. 
The function should print the data type of each argument, 
and return True if all three arguments are of the same data type, and False otherwise.

For example, if the function is called with 
x = 42, y = 3.14, and z = "Hello, world!", 
it should output:

x is of type <class 'int'>
y is of type <class 'float'>
z is of type <class 'str'>

'''

#Template

def check_types(x, y, z):
    """
    Returns the data types of the arguments x, y, and z.
    """
    return (type(x), type(y), type(z))


# Call the function with some values


# Print the result
