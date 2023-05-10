'''
A decorator is a function that modifies the behavior of another function. 
In this case, the add_two decorator takes a function as an argument, 
creates a new function wrapper that calls the original 
function and adds 2 to its return value, and returns the wrapper function.

The @add_two syntax is a shortcut for applying the add_two decorator 
to the get_five function. This means that when get_five is called, 
it will first be passed through the add_two decorator, which will modify its behavior.

When we call get_five() and print the result, we get 7 because the 
add_two decorator adds 2 to the original return value of 5.
'''

def add_two(func):
    def wrapper():
        return func() + 2
    return wrapper

@add_two
def get_five():
    return 5

print(get_five())  # Output: 7
