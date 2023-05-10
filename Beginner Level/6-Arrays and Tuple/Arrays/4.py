#Creating a two-dimensional array

# Create a two-dimensional array
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# Accessing elements in a two-dimensional array
first_element = matrix[0][0]  # Accessing the first element in the first row
last_element = matrix[-1][-1]  # Accessing the last element in the last row

# Modifying elements in a two-dimensional array
matrix[1][1] = 0  # Changing the middle element in the middle row to 0
matrix.append([10, 11, 12])  # Adding a new row to the end of the matrix

# Looping through a two-dimensional array
for row in matrix:
    for element in row:
        print(element)

# Slicing a two-dimensional array
first_two_rows = matrix[:2]  # Getting the first two rows of the matrix
last_two_columns = [row[-2:] for row in matrix]  # Getting the last two columns of the matrix

# Printing the arrays
print(matrix)
print(first_two_rows)
print(last_two_columns)
