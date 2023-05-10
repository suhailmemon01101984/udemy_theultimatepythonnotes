# Exercise: Type checking



#One way to solve this problem

def check_types(x, y, z):
    """
    Returns the data types of the arguments x, y, and z as a tuple.
    """
    return (type(x), type(y), type(z))

# Call the function with some values
result = check_types(42, 3.14, "Hello, world!")

# Print the result
print(result)  # Output: <class 'int'> <class 'str'> <class 'list'>
