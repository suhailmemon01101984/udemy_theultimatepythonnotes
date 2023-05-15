#Example 1: Generator function to return squares of numbers


def squares(n):
    for i in range(n):
        yield i**2

# Using the generator function
for square in squares(5):
    print(square)
