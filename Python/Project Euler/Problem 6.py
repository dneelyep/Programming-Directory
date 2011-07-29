#Problem 6 - CORRECT!
#The sum of the squares of the first ten natural numbers is,
    #1squared + 2squared + ... + 10squared = 385

#The square of the sum of the first ten natural numbers is,
    #(1 + 2 + ... + 10)squared = 55squared = 3025

#Hence the difference between the sum of the squares of
    #the first ten natural numbers and the square of the sum is
    #3025 - 385 = 2640.2640

#Find the difference between the sum of the squares of the first
#one hundred natural numbers and the square of the sum.


#Find sum of the squares of 1-100

basenumber = 0
squareofthesum = 0
sumsquaretotal = 0
squaresumtotal = 0

while basenumber < 100:
    basenumber = basenumber + 1
    #print basenumber
    
    sumofthesquares = basenumber * basenumber
    print sumofthesquares
    sumsquaretotal = sumsquaretotal + sumofthesquares
    print sumsquaretotal

    squareofthesum = squareofthesum + basenumber
    print squareofthesum
    squaresumtotal = squareofthesum * squareofthesum
    print squaresumtotal

total = squaresumtotal - sumsquaretotal
print total
