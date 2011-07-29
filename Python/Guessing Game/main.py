import random

def intro():
    print "Welcome to Guessing Game! To play the game, guess a number between 1 and 100."
    number = random.random
    guess()

def guess():
    guess = raw_input("Please enter a number: ")

    if guess == number:
        print "Congrats, you win!"
        intro()
    elif guess < number:
        print "A little higher, chea"
        guess()
    elif guess > number:
        print "MOARLOWERPLOX"
        guess()

intro()
