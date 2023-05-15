# Exercise: Compare and Print

'''
 Write a Python program that takes two integer inputs x and y f
 rom the user and compares them. If x is greater than y, print "x is greater than y", 
 otherwise, print "x is less than or equal to y". 
 If x and y are equal, print "x is equal to y".
'''

x=int(input("Please enter value of x: "))
y=int(input("Please enter value of y: "))

if(x>y):
    print("x is greater than y")
elif(y>x):
    print("y is greater than x")
else:
    print("x is equal to y")
