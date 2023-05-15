# Exercise: four functions to add, subtract, multiply, and divide two numbers:



#One way to sole it 

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y


'''
These functions take two arguments, x and y, 
and return the result of the corresponding mathematical operation. 
The divide function checks if the second argument y is zero before performing the division, 
and raises a ValueError if it is, to avoid a division by zero error.
'''