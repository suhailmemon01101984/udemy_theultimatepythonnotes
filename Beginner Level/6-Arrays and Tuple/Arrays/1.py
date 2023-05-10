'''
Arrays

An array is a data structure that stores a collection of elements, 
each identified by an index or a key. In Python, arrays are implemented as lists.
'''

#Example 1: Creating an array
# Create an array of integers
numbers = [1, 2, 3, 4, 5]

# Create an array of strings
fruits = ["apple", "banana", "orange", "grape"]



#Example 2: Accessing elements in an array
# Get the first element of the numbers array
first_number = numbers[0]

# Get the last element of the fruits array
last_fruit = fruits[-1]



#Example 3: Modifying elements in an array
# Change the value of the third element in the numbers array
numbers[2] = 10

# Add a new element to the end of the fruits array
fruits.append("pineapple")


#Example 4: Looping through an array
# Print all the elements of the numbers array
for num in numbers:
    print(num)

# Check if "banana" is in the fruits array
for fruit in fruits:
    if fruit == "banana":
        print("Found it!")


#Example 5: Slicing an array
# Get the first three elements of the numbers array
first_three_numbers = numbers[:3]

# Get the last two elements of the fruits array
last_two_fruits = fruits[-2:]


print(first_three_numbers)
print(last_two_fruits)
