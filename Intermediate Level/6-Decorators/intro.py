#Introduction to Python Decorators

'''
Decorators are commonly used to implement cross-cutting concerns, 
such as logging, caching, or security, that apply to multiple functions or classes.
'''

#Syntax

#The syntax for using decorators in Python is:

'''
@decorator
def function():
    pass


#This syntax is equivalent to the following:
def function():
    pass
function = decorator(function)

'''
