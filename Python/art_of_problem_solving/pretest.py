#1. Write a program to play a simple guessing game. The computer should pick a random number
#between 1 and 500. The user should enter a guess. The computer should tell the user if the
#guess was too low, too high, or correct. Repeat until the user guesses the number correctly.
#When the game is over, give the player a ranking based on how many guesses were made.
import random

correct_num = random.randint(1,500)

def ask_for_guess():
    guess = raw_input("Enter a guess: ")
    print guess
    if guess == correct_num:
        print "Your guess was correct!"
    elif guess < correct_num:
        print "Your guess was too low! Try again plox."
        ask_for_guess()
    elif guess > correct_num:
        print "Too high. Try again."
        ask_for_guess()

ask_for_guess()
