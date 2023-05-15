import random

def guess_number():
    number = random.randint(1, 100)
    guesses = 0
    while True:
        guess = int(input("Guess a number between 1 and 100: "))
        guesses += 1
        if guess == number:
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            break
        elif guess < number:
            print("Your guess is too low. Try again.")
        else:
            print("Your guess is too high. Try again.")

guess_number()
