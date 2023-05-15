# Example 1: Handling a specific exception


'''

we are handling a specific exception (ZeroDivisionError) that can occur when trying to divide by zero. 
If this exception is raised, the program will print "Cannot divide by zero".
'''
try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print("The result is:", result)
except ZeroDivisionError:
    print("Cannot divide by zero")

