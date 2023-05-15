# Example 2: Handling multiple exceptions
'''
we are handling multiple exceptions (ValueError and TypeError) that can occur when trying to add an integer and a string. 
If either of these exceptions is raised, the program will print a corresponding error message.
'''


try:
    x = int(input("Enter a number: "))
    y = input("Enter a string: ")
    z = x + y
except ValueError:
    print("Invalid input for integer")
except TypeError:
    print("Cannot add integer and string")