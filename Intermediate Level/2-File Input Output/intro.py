#File Input/Output in Python
'''
Python provides a variety of ways to read from and write to files. 
Some common file formats include plain text files, JSON files, and CSV files. 
In this section, we'll cover the basics of file input/output in Python.
'''
#################################################################


#Opening a File
'''
Before we can read from or write to a file, we need to open it. 
We can use the built-in open() function to do this. 
The open() function takes two arguments: 
the name of the file, and the mode in which we want to open it.
'''
#Example
file = open("filename.txt", "r")
'''
In the above example, we open a file named "filename.txt" in read mode ("r"). 
The open() function returns a file object, 
which we can then use to read from or write to the file.
'''
#################################################################


#Reading from a File
'''
Once we've opened a file, we can read from it using the read() method of the file object.
'''
#Example
file = open("filename.txt", "r")
contents = file.read()
print(contents)
'''
In the above example, we read the entire contents of the file into a 
variable named contents. 
We can then print out the contents of the file using the print() function.
'''

#################################################################
#We can also read from a file line by line using the readline() method.
#Example
file = open("filename.txt", "r")
line = file.readline()
print(line)
'''
In the above example, we read the first line of the file into a variable named line. 
We can then print out the line using the print() function. 
We can repeat this process to read in the entire file line by line.
'''


#################################################################
#Writing to a File
'''
We can write to a file using the write() method of the file object.
'''
#Example
file = open("filename.txt", "w")
file.write("Hello, world!")
file.close()
'''
In the above example, we open a file named "filename.txt" in write mode ("w"),
write the string "Hello, world!" to the file using the write() method, 
and then close the file using the close() method.
'''


#################################################################
#JSON Files

'''
JSON (JavaScript Object Notation) is a lightweight data interchange 
format that is easy for humans to read and write, and easy for machines 
to parse and generate. Python has built-in support for working with JSON 
files using the json module.

To read from a JSON file, we can use the json.load() function.
'''
#Example
import json

with open("filename.json", "r") as file:
    data = json.load(file)
    print(data)
'''
In the above example, we use the with statement to open the file "filename.json" 
in read mode ("r"). We then use the json.load() function to load the 
contents of the file into a variable named data. We can then print out 
the contents of the file using the print() function.
'''


#################################################################
#To write to a JSON file, we can use the json.dump() function.
#Example
import json

data = {"name": "Alice", "age": 30}

with open("filename.json", "w") as file:
    json.dump(data, file)

'''
In the above example, we create a Python dictionary named data that contains 
two key-value pairs. We then use the with statement to open the 
file "filename.json" in write mode ("w"). 
We then use the json.dump() function to write the contents of 
the dictionary to the file.
'''