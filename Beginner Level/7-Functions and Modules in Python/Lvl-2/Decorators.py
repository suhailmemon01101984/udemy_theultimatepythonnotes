'''
This is an example of how to define a function that 
accepts a variable number of arguments, using the *args syntax. 
The function is called print_args and takes any number of arguments.

The function definition starts with def, 
followed by the function name print_args, 
and then the parameter list inside parentheses. 
In this case, we have a single parameter, which is denoted by *args. 
This means that the function can accept any number of arguments, 
which will be collected into a tuple called args.

Inside the function, we use a for loop to iterate over each 
argument in the args tuple, and then print it to the console 
using the print function.

To call the function, we simply pass in the arguments separated by 
commas, as shown in the example print_args(1, "two", True). 

'''

def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, "number 3", True)  # Output: 1 2 number 3 True
