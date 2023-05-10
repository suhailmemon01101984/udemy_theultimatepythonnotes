# Read File in Python

# There are a couple of ways to read a file in Python. 
# One way is to use the open() function to create a file object,
# and then use the read() method to read the contents of the file.

# Example 1: Using open() and read()
f = open("input.txt", "r")
print(f.read())
f.close()

# Another way to read a file is to use the with statement. 
# This creates a context in which the file is automatically closed when the block is exited.

# Example 2: Using with statement
with open("input.txt", "r") as file:
    lines = file.readlines()
    
for line in lines:
    print(line.strip())
