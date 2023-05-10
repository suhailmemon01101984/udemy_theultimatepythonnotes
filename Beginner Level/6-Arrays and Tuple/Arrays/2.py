# Creating an array of names
names = ["Alice", "Bob", "Charlie", "Dave", "Eve"]

# Accessing elements in an array
first_name = names[0]  # Accessing the first element in the array
last_name = names[-1]  # Accessing the last element in the array

# Modifying elements in an array
names[2] = "Carol"  # Changing the third element in the array to "Carol"
names.append("Frank")  # Adding a new element to the end of the array

# Looping through an array
for name in names:
    print(name)

# Slicing an array
first_two_names = names[:2]  # Getting the first two elements of the array
last_three_names = names[-3:]  # Getting the last three elements of the array

# Printing the arrays
print(names)
print(first_two_names)
print(last_three_names)


'''
In this example, we start by creating an array of names. We then access the first and last elements of the array using indexing. 
Next, we modify the third element in the array and add a new element to the end of the array. We then loop through the array and print each element. 
Finally, we use slicing to create new arrays that contain a subset of the original array, and we print all three arrays to the console.

'''