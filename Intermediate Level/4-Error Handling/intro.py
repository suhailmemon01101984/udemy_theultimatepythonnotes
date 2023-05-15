#Introduction to Error Handling in Python

'''
Error handling is an essential part of programming in any language, including Python. 
In Python, we use the try and except statements to handle errors that may occur during program execution.

When an error occurs in Python, it generates an exception object that contains information about the error. 
This exception object is then passed to the except statement, which handles the error and prevents the program from crashing.
'''


#Syntax of try-except
try:
    pass
    # code block to be executed
except :
    # code block to handle the exception
    pass

'''
The try block contains the code that may raise an exception, while the except block contains the code to handle the exception. 
The ExceptionType in the except block specifies the type of exception to be handled. 
If an exception of this type occurs in the try block, then the code in the except block is executed.
'''

#Types of Exceptions

'''
In Python, there are many types of exceptions that may occur during program execution. Here are some of the most common ones:

    SyntaxError: This occurs when there is a problem with the syntax of your code. For example, if you forget to close a parenthesis or put a colon in the wrong place.
    TypeError: This occurs when you try to perform an operation on two objects of different types. For example, if you try to add an integer and a string.
    NameError: This occurs when you try to use a variable that has not been defined.
    ZeroDivisionError: This occurs when you try to divide a number by zero.

'''


#Raising Exceptions

x = -5

if x < 0:
    raise Exception("x cannot be negative") #This code raises an exception if x is negative.


#Finally Block
'''
In addition to the try and except blocks, you can also use a finally block. 
This block contains code that will always be executed, whether an exception is raised or not. Here's an example:
'''

try:
    # code block to be executed
    pass
except :
    # code block to handle the exception
    pass
finally:
    # code block to be executed always
    pass
