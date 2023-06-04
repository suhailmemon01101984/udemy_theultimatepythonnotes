# Define a function named average_multiples_of_3 that takes a list of integers as input
'''
def average_multiples_of_3(numbers):
    # Initialize variables to hold the sum and count of multiples of 3
'''
# Loop through the input list and check each number for multiples of 3

# If the number is a multiple of 3
# Add it to the sum of multiples of 3
# Increment the count of multiples of 3

# Check if there are any multiples of 3 in the list

# If there are no multiples of 3, return -1

# Calculate and return the average of multiples of 3

def average_multiples_of_3(numbers):
    sum=0
    count=0
    for i in range(len(numbers)):
        if int(numbers[i])%3==0:
            count=count+1
            sum=sum+int(numbers[i])

    if count==0:
        return -1
    else:
        print(f"Average of the numbers that are multiple of 3: {sum/count}")


input_string=input("Enter list of integers separated by comma: ")
numbers=input_string.split(",")
print(type(numbers))
average_multiples_of_3(numbers)