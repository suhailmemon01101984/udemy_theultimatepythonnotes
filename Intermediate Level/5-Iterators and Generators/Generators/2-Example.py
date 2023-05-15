#Example 2: Generator expression to return odd numbers from a list

numbers = [1, 2, 3, 4, 5]

# Using the generator expression
odd_numbers = (n for n in numbers if n % 2 != 0)
for number in odd_numbers:
    print(number)
