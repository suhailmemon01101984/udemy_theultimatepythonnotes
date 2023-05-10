# Exercise: Compare and Print

'''
In this program, we first take two integer 
inputs x and y from the user using the input() function. 
Then, we use an if-elif-else statement to compare x and y and 
print the appropriate message based on the comparison. 
10If x is greater than y, we print "x is greater than y". If x is equal to y, 
we print "x is equal to y". 
Otherwise, we print "x is less than or equal to y".
'''

#One Solution Example

x = int(input("Enter x: "))
y = int(input("Enter y: "))

if x > y:
    print("x is greater than y")
elif x == y:
    print("x is equal to y")
else:
    print("x is less than y")



