# An implementation of Euclid's algorithm for finding the greatest common divisor of a pair of positive integers.
# FIXME: Run the time command (or whatever it is) on the program when complete and test the optimization in TAOCP, where you check whether or not m < n before running the program.
print "Hai there!"
print "This program finds the greatest common divisor of a pair of positive integers."

print "Please enter the first integer: "
first_integer = raw_input()

print "Please enter the second integer: "
second_integer = raw_input()

# Convert the input from strings into integers
first_integer  = int(first_integer)
second_integer = int(second_integer)

print "First integer: "
print first_integer
print "Second integer: "
print second_integer

print "\nNow for the algorithm!"

while first_integer % second_integer != 0:
    remainder = first_integer % second_integer
    first_integer = second_integer
    print "\nFirst integer now becomes: "
    print first_integer
    second_integer = remainder
    print "Second integer now becomes: "
    print second_integer
    print "Remainder is: "
    print remainder

print "The greatest common divisor is: "
print second_integer



#def quitgame():
 #   print "\nWould you like to >>>close<<< the game completely, or return to the main >>>menu<<< ?"
  #  inputprompt()
   # if playerinput == 'close':
    #    print "Game closing nao."
#           MAKE THIS ACTUALLY CLOSE THE GAME
#    elif playerinput == 'menu':
 #       menu()
  #  else:
   #     print "\nYou entered something incorrectly. Please try again."
