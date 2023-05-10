#Control Structures


'''

Control structures allow you to control the flow of your program based on certain conditions.

If/else statements: 
These allow you to execute different blocks of code 
depending on whether a certain condition is true or false.

Loops: 
These allow you to execute a block of code multiple times.

Here's an example of how to use these control structures:
'''


x = 5
if x > 0: #if x is greater than 0
    print("x is positive") #print that x is positive
else: #if x is not the if statement
    print("x is zero or negative") #print that x is zero or negative

my_list = [1, 2, 3, 4, 5] #Create a list of numbers
for num in my_list: #Creating a for loop to run over each number in the list
    print(num) # printing each number on its own line



'''
A dictionary is a collection of key-value pairs. 
Each key is associated with a value, and you can use the key to access the value. 
Dictionaries are created using curly braces and separated by commas. 

For example:

'''

my_dict = {"name": "John", "age": 25, "is_student": True} 

#Creating a for loop that have two key values 
#Since the (my_dict) is a shape of two, e.g (name : john) the for loop has the same shape
#key = name, age, is_student
#Value = John, age, True

for key, value in my_dict.items(): 
    print(key, value)
