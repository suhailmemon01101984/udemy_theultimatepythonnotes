#String formatting


# Define a variable "name" with a string value
name = "Alice"

# Define a variable "age" with a numerical value
age = 30

# Print a string that includes the values of "name" and "age" using an f-string
print(f"My name is {name} and I am {age} years old.")

# Print a string that includes the values of "name" and "age" using the format() method
print("My name is {} and I am {} years old.".format(name, age))

"""
The format() method is a built-in Python function 
that allows you to format strings by inserting values 
into placeholders within the string.

In the example code above, we have a string with 
two placeholders: {}. We want to insert the values 
of the name and age variables into those placeholders.

We call the format() method on the string, 
and pass the values we want to insert as arguments to the method. 
In this case, we pass name and age. The format() method replaces the 
placeholders in the string with these values, and returns a new string 
with the replacements made.

The format() method provides a lot of flexibility when it 
comes to formatting strings. You can use numbered placeholders, 
named placeholders, and even specify formatting options for each 
value you want to insert.
"""