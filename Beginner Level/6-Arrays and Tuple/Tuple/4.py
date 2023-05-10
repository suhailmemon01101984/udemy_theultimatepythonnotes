# Example 4: Using tuples in functions
# Define a function that returns multiple values as a tuple
def calculate_rectangle_area_and_perimeter(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return (area, perimeter)

# Call the function and unpack the returned tuple
rectangle_area, rectangle_perimeter = calculate_rectangle_area_and_perimeter(4, 6)

# Print the area and perimeter
print("Area:", rectangle_area)
print("Perimeter:", rectangle_perimeter)
