"""
You can also use variable-length arguments in a function. 
These are arguments that can take any number of values. 
For example:
"""

def add_numbers(*args):
    result = 0
    for num in args:
        result += num
    return result

result1 = add_numbers(1, 2, 3)
result2 = add_numbers(10, 20, 30, 40, 50)

print(result1)  # Output: 6
print(result2)  # Output: 150