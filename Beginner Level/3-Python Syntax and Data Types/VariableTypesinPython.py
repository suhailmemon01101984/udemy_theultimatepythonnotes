# Variable Types in Python

'''
This program demonstrates various types of variables in Python, 
including integers, floats, strings, and booleans. 
It also shows how to use the type() 
function to get the type of a variable, 
and how to convert between different types 
using functions like str(), int(), and float().

The program also demonstrates various arithmetic 
and string operations that can be performed on variables, 
including 
addition, 
subtraction, 
multiplication, 
division, 
modulo, 
integer division, 
exponentiation, 
string concatenation, 
and string repetition
'''


################################################################
#Type shows the type of a variable (Integer or Float or String)

# Integer
x = 42
print(x, type(x)) 

# Float
y = 3.14
print(y, type(y))

# String
z = "Hello, world!"
print(z, type(z))

# Boolean
a = True
print(a, type(a))

# Type conversion
x = str(x)
print(x, type(x))

y = int(y)
print(y, type(y))

z = float(len(z))
print(z, type(z))

# Arithmetic operations
x = 10
y = 3
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x // y)
print(x ** y)

# String operations
a = "Hello"
b = "world"
print(a + ", " + b + "!")
print(a * 3)


"""
When you run this program, you should see output like this:



42 <class 'int'>
3.14 <class 'float'>
Hello, world! <class 'str'>
True <class 'bool'>
42 <class 'str'>
3 <class 'int'>
13.0 <class 'float'>
13
7
30
3.3333333333333335
1
3
1000
Hello, world!
HelloHelloHello

"""
