#Exercise 1: Guess the Number

'''

Write a Python program that generates a random number 
between 1 and 100 and allows the user to guess the number. 
The program should tell the user if their guess is too high or too low, 
and keep track of the number of guesses it takes the user to guess the number.
'''


'''
Instructions:

    Generate a random number between 1 and 100 using the random module.
    Ask the user to guess the number.
    If the user's guess is too high, print "Too high! Try again."
    If the user's guess is too low, print "Too low! Try again."
    If the user's guess is correct, print "Congratulations! You guessed the number."
    Allow the user to keep guessing until they guess the number correctly.

'''

#Example Output:
'''
Guess the number between 1 and 100: 50
Too high! Try again.
Guess the number between 1 and 100: 25
Too low! Try again.
Guess the number between 1 and 100: 37
Too high! Try again.
Guess the number between 1 and 100: 32
Too low! Try again.
Guess the number between 1 and 100: 34
Congratulations! You guessed the number.
'''

'''
Bonus:

    Keep track of how many guesses it takes the user to guess the number, 
    and print the number of guesses when the user guesses the number correctly.
    
    Allow the user to choose the range of numbers to guess from.

'''
import random

guess_right_ind=0
num_of_guesses=0


startingnumber,endingnumber=input("Please provide the range of numbers to guess from(x,y): ").split(",")
#print(startingnumber)
#print(endingnumber)

while guess_right_ind==0:
    guessnumber=input(f"Guess the number between {startingnumber} and {endingnumber}: ")
    randomnum=random.randint(int(startingnumber),int(endingnumber))
    if (int(guessnumber)>randomnum):
        print("Too high! Try again.")
        num_of_guesses=num_of_guesses+1
    elif(int(guessnumber)<randomnum):
        print("Too low! Try again.")
        num_of_guesses=num_of_guesses+1
    else:
        print("Congratulations! You guessed the number.")
        num_of_guesses=num_of_guesses+1
        guess_right_ind=1

print(f"It took you {num_of_guesses} guesses to guess the right number.")
