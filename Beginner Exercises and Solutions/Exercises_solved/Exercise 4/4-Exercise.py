# Exercise: Calculator with File Output

'''
Write a program that asks the 
user to enter two numbers and then performs 
basic addition.
The program should then write the results 
to a file called "results.txt" in the following format:

The result is: result
'''

num1=input('please enter first number: ')
num2=input('please enter second number: ')
result=float(num1) + float(num2)
with open('results.txt','w') as f:
    f.write('The result is: '+ str(result))
