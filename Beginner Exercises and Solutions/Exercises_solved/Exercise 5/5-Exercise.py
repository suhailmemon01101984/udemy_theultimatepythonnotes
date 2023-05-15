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

def check_types(x,y,z):
    print("x is of type ",type(x))
    print("y is of type ", type(y))
    print("z is of type ", type(z))
    if(type(x)==type(y)==type(z)):
        return True
    else:
        return False

bool_value=check_types(1,2,3)

print(bool_value)
