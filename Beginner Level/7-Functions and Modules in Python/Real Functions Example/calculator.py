#Here's an example of a simple calculator function that can perform 
#addition, subtraction, multiplication, and division:

def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: division by zero"
        else:
            return num1 / num2
    else:
        return "Error: unsupported operator"



result = calculator(5, 3, "+")
print(result)  # Output: 8

result = calculator(5, 3, "-")
print(result)  # Output: 2

result = calculator(5, 3, "*")
print(result)  # Output: 15

result = calculator(5, 3, "/")
print(result)  # Output: 1.6666666666666667

result = calculator(5, 0, "/")
print(result)  # Output: Error: division by zero

result = calculator(5, 3, "%")
print(result)  # Output: Error: unsupported operator



'''
This function takes in three arguments: 
num1, num2, and operator. 
The operator argument specifies which operation to perform, 
with + for addition, - for subtraction, * for multiplication, and / for division. 
If an unsupported operator is specified, the function returns an error message.
'''