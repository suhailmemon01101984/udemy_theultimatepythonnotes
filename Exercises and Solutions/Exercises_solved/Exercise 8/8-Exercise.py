
# Exercise: Text File Reader

'''

Create an input.txt file

Write a program that reads a text file named "input.txt" 
and prints its contents to the console.


Note: Make sure that the "input.txt" file exists in the same directory as your Python script.
If the file is located in a different directory, 
you will need to provide the full file path in the open() function.
'''
import os.path

str="this is my second file: Suhail"
dir="/Users/suhailmemon/Documents/MACBOOKPRO/dell laptop/Desktop/git/udemy_theultimatepythonnotes/Exercises and Solutions/Exercises_solved/Exercise 8"
file="input.txt"
full_path=os.path.join(dir,file)
print(full_path)
with open(full_path,'w') as f:
    f.write(str+'\n')
f.close()

with open(full_path,'r') as f:
    print(f.read())
f.close()


