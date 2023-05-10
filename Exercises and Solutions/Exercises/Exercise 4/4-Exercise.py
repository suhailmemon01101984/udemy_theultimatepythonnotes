# Exercise: Calculator with File Output

'''
Write a program that asks the 
user to enter two numbers and then performs 
basic addition.
The program should then write the results 
to a file called "results.txt" in the following format:

The result is: result
'''


#Template

# Prompt the user to enter two numbers


# Perform the calculation

# Write the result to a file
with open("results.txt", "w") as file:
    file.write(str(result))

# Print the result to the console

