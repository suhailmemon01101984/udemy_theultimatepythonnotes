"""
This is a function called greet that takes two parameters: 
name and greeting. The greeting parameter is optional and 
has a default value of "Hello" if no value is provided when the function is called.

The function uses the print statement to output the greeting and the name. 
If no greeting is provided, it defaults to "Hello".

The function is called twice: first with only the name parameter provided 
(resulting in the output "Hello Alice"), 
and then with both name and greeting parameters provided 
(resulting in the output "Hi Bob").

"""


def greet(name, greeting="Hello"):
    print(greeting, name)

greet("Alice")  # Output: Hello Alice
greet("Bob", "Hi")  # Output: Hi Bob



