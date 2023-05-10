#This function takes in three arguments: num1, num2, and operator. The operator argument specifies which operation to perform, with + for addition, - for subtraction, * for multiplication, and / for division. 
#If an unsupported operator is specified, the function returns an error message.

def reverse_string(string):
    """Reverses the given string."""
    return string[::-1]


my_string = "hello world"
reversed_string = reverse_string(my_string)
print(reversed_string)  # Output: "dlrow olleh"
