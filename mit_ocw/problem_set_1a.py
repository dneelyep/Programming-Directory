# Computing Prime Numbers
#A common type of computation is the generate-and-test method, in which one systematically generates potential solutions to a problem, and then applies a sequence of one or more tests to determine if the proposed solution is in fact valid. While one could in principle (and under some circumstances one must) generate potential solutions randomly or according to some probability distribution, often it is more efficient to devise a systematic method for generating all candidate solutions.

# Problem 1.
# Write a program that computes and prints the 1000th prime number.
# Hints:
#To help you get started, here is a rough outline of the stages you should probably follow in writing your code:
#   1. Initialize some state variables
#   2. Generate all (odd) integers > 1 as candidates to be prime
#   3. For each candidate integer, test whether it is prime
#     1. One easy way to do this is to test whether any other integer > 1 evenly divides the candidate with 0 remainder. To do this, you can use modular arithmetic, for example, the expression a%b returns the remainder after dividing the integer a by the integer b.
#     2. You might think about which integers you need to check as divisors – certainly you don’t need to go beyond the candidate you are checking, but how much sooner can you stop checking?
# 4. If the candidate is prime, print out some information so you know where you are in the computation, and update the state variables
# 5. Stop when you reach some appropriate end condition. In formulating this condition, don’t forget that your program did not generate the first prime (2). 

#If you want to check that your code is correctly finding primes, you can find a list of
#primes at http://primes.utm.edu/lists/small/1000.txt.

current_int = 1

def check_int(integer):
  counter = 2
  total_num = 0
  while total_num <= 10000:
      if counter >= integer / 2:
#          print str(integer) + " IS a prime number."
           integer += 2
           counter = 2
           total_num += 1
 #          print str(total_num) + " primes so far."

       else:
           if integer % counter == 0:
 #              print str(integer) + " is NOT a prime number."
               integer += 2
               counter = 2
           else:
               counter += 1
#              print "Incrementing counter to " + str(counter)

check_int(1)
