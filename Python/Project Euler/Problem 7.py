#Problem 7
#By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#we can see that the 6^(th) prime is 13.

#What is the 10001st prime number?


#So, create a variable (currentnum) for the number being tested, = 2 at beginning
#   Check if it's prime. If so, add 1 to the primenum variable, then increment.
#   Else, increment.
#   If primenum = 10001, print primenum

#Set currentnum to 2. Check if any of the numbers below it are evenly divisible.
#  If so, continue. If not, increment the value of a counter that counts the
#  number of prime it is. Then continue. Do this until the counter = 10001.


currentnum = 2
primenum = 0

def checkprime():
    checknum = 2
    while checknum < currentnum:
        if currentnum % checknum == 0:
            return 0
            checknum = checknum + 1
        else:
            checknum = checknum + 1

while primenum < 10002:
    if checkprime():
        primenum = primenum + 1
        print currentnum
        currentnum = currentnum + 1
    else:
        currentnum = currentnum + 1
        print currentnum

#currentnum = 2
#dividingnum = 2
#counter = 0

#while counter <= 10001:
#    while currentnum >= dividingnum:
#        if currentnum % dividingnum == 0:
#            dividingnum += 1
#        elif currentnum == dividingnum:
#            counter += 1
#        else:
#            dividingnum += 1
#    print currentnum
#    print counter
