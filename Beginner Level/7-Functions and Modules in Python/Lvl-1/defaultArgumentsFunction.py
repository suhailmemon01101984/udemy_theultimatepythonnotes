"""
Functions can also have default arguments. 
These are arguments that have a default value, 
which is used if the function is called without providing that argument. 

For example:
"""

def repeat_string(string, times=3):
    return string * times

result1 = repeat_string("hello")
result2 = repeat_string("world", 5)

print(result1)  # Output: hellohellohello
print(result2)  # Output: worldworldworldworldworld
