'''
Tuples

A tuple is an immutable sequence of elements, similar to a list. 
However, once a tuple is created, 
its elements cannot be modified.
'''

#Example 1: Creating a tuple
# Create a tuple of integers
numbers = (1, 2, 3, 4, 5)

# Create a tuple of strings
fruits = ("apple", "banana", "orange", "grape")




#Example 2: Accessing elements in a tuple
# Get the first element of the numbers tuple
first_number = numbers[0]

# Get the last element of the fruits tuple
last_fruit = fruits[-1]




#Example 3: Looping through a tuple
# Print all the elements of the numbers tuple
for num in numbers:
    print(num)

# Check if "banana" is in the fruits tuple
for fruit in fruits:
    if fruit == "banana":
        print("Found it!")



#Example 4: Unpacking a tuple
# Unpack the first two elements of the numbers tuple
a, b = numbers[:2]

# Unpack the first and last elements of the fruits tuple
first, *middle, last = fruits



#Example 5: Converting a tuple to a list
# Convert the numbers tuple to a list
numbers_list = list(numbers)
print(numbers_list)

###This will result into and error messages
# Add a new element to the end of the fruits tuple (not possible)


#fruits.append("pineapple")  # Raises a TypeError

