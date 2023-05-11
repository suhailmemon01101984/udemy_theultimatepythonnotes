# Exercise: User input

'''
Write a Python program that asks the user to input two numbers and 
then performs addition on those numbers. 

The program should display the results of each operation to the user.
'''

#Template

# Take user input (2 variable eg. num1, num2)
num1=input("Please enter first number: ")
print("thanks for providing your input. The first number you entered is " + num1)

num2=input("Please enter second number: ")
print("thanks for providing your input. The second number you entered is " + num2)

# add num 1 and num 2

sum_of_two_numbers=float(num1)+float(num2)

# Print the result

print("the sum of these two numbers is: ", sum_of_two_numbers)
