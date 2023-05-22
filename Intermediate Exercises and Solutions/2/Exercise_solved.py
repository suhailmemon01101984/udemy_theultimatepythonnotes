#Exercise 2: Word Jumble Game

'''

Write a program that picks a random word from a list of words and jumbles up its letters. 
The player must guess the original word.
'''


'''
Here's an outline of the program:
    Define a list of words.
    Pick a random word from the list.
    Jumble up the letters of the word.
    Print the jumbled word and ask the player to guess the original word.
    Keep track of the number of guesses the player makes.
    If the player guesses correctly, print a congratulatory message and the number of guesses it took.
    If the player runs out of guesses, print a message revealing the original word.
'''

import random
list_of_words=["constantine","coconut","americano","espresso"]
number_of_guesses_left=3
number_of_guesses_done=0
game_finish_ind=0
index=random.randint(0,3)
random_word=list(list_of_words[index])
random.shuffle(random_word)
jumbled_word=''.join(random_word)

while game_finish_ind==0 and number_of_guesses_left>0:
    guessed_word=input(f"The jumbled word is: {jumbled_word}. Please guess the original word you have {number_of_guesses_left} guesses: ")
    number_of_guesses_left = number_of_guesses_left - 1
    number_of_guesses_done=number_of_guesses_done+1
    if(guessed_word==list_of_words[index]):
        print(f"Congratulations, you are correct! It took you {number_of_guesses_done} guesses to win!")
        game_finish_ind=1
    elif number_of_guesses_left==0:
        print(f"Sorry, bad guess. You have run out of guesses. The original word is: {list_of_words[index]}")
    else:
        print("Sorry, bad guess. Please try again")




