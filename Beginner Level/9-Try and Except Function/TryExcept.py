'''
In this example, the user is prompted to enter two numbers. 
The program attempts to divide the first number by the second number and print the result. 
However, there are two potential exceptions that could occur:

    If the user enters 0 as the second number, a ZeroDivisionError will occur.
    If the user enters something other than a number for either input, a ValueError will occur.


To handle these exceptions, the program uses a try-except block. 

The try block contains the code that may raise an exception. If an exception occurs, 
the program moves to the appropriate except block and executes the code within it. 
In this example, if a ZeroDivisionError occurs, the program prints an error 
message saying that division by zero is not allowed. If a ValueError occurs, 
the program prints an error message saying that the input was invalid.

'''


try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("Result: ", result)
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
except ValueError:
    print("Error: Invalid input. Please enter a number.")


#except can be for
'''
except keyError 
except TypeError
except NameError
except RuntimeError
and more 

'''