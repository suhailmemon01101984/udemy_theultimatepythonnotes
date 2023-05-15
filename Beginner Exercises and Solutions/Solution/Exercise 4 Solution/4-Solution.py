# Exercise: Calculator with File Output

# Prompt the user to enter two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Perform the calculation
result = num1 + num2

# Write the result to a file
with open("output.txt", "w") as file:
    file.write(str(result))

# Print the result to the console
print("The result is:", result)
