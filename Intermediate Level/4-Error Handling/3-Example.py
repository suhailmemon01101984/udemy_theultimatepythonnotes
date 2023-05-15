# Example 3: Handling any exception

'''
we are using a generic except block to handle any type of exception that may occur. 
We are also using the as keyword to assign the exception object to a variable e, 
so that we can print more information about the exception.

'''

try:
    a = [1, 2, 3]
    print(a[3])
except Exception as e:
    print("An error occurred:", e)