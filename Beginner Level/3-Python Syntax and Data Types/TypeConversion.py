#Type conversion
#Initialize the variables

x = 42
y = 3.14
z = "Hello, world!"
#Print the types of the variables before conversion

print('\nBefore')
print(type(x))
print(type(y))
print(type(z))
#Perform the type conversions

print("\n-------------\n")
print('After')
x = str(x) # convert x to a string
print(x, type(x))
y = int(y) # convert y to an integer
print(y, type(y))
z = float(len(z)) # convert the length of z to a float
print(z, type(z))


#Explanation of code
'''
We initialize three variables with different data types

We print the types of these variables before performing any conversions

We perform the following conversions:
    x is converted from an integer to a string using str()
    y is converted from a float to an integer using int()

the length of z is first computed using len() and then converted from an integer to a float using float()

We print the new values and types of the variables after the conversions are performed

'''
