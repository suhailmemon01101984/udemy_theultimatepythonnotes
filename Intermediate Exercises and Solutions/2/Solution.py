import random

# Define a list of words
words = ['apple', 'banana', 'orange', 'pear', 'grape', 'pineapple']

# Pick a random word from the list
word = random.choice(words)

# Jumble up the letters of the word
jumbled_word = ''.join(random.sample(word, len(word)))

# Print the jumbled word and ask the player to guess the original word
print(f"The jumbled word is: {jumbled_word}")
guess = input("Guess the original word: ")

# Keep track of the number of guesses the player makes
num_guesses = 1

# Keep asking for guesses until the player guesses correctly or runs out of guesses
while guess.lower() != word.lower() and num_guesses < 3:
    print("Incorrect guess, try again.")
    guess = input("Guess the original word: ")
    num_guesses += 1

# Print the result
if guess.lower() == word.lower():
    print(f"Congratulations! You guessed the word in {num_guesses} guesses.")
else:
    print(f"Sorry, you ran out of guesses. The word was {word}.")
