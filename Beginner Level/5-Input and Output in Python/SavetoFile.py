'''

This code creates a new file called "output.txt" in the current working directory and writes the string "Hello, world!" to it. 
If the file already exists, 
this code will overwrite its contents. 
The with statement ensures that the file is closed properly after the write operation is completed.
'''


with open("output.txt", "w") as file:
    file.write("Hello, world!")
