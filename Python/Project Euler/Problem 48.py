#Problem 14

#The following iterative sequence is defined for the set of positive integers:

#   n → n/2 (n is even)
#   n → 3n + 1 (n is odd)

#Using the rule above and starting with 13, we generate the following sequence:    
#13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1

#It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

#Which starting number, under one million, produces the longest chain?

#NOTE: Once the chain starts the terms are allowed to go above one million.


#So: set a starting number, starting at 1,000,000.
    #Perform the given operations on this number, checking how many steps its taking while doing so.
        #If the number of steps taken is larger than any previous number, this number becomes the number with largest chain.
            #Decrement the starting number and try again.

currentnum = 100

def operations():
    while currentnum != 1:
        #set n equal to currentnum's value
        n = currentnum
        #do if number is even
        if currentnum % 2 == 0:
            currentnum =  / 2
            print n
        #do if number is odd
        elif currentnum % 2 != 0 and currentnum != 1:
            print "FALSE"
        #do when number reaches one
        else:
            print "IT'S DA ONE!"

while currentnum > 0:
    #perform operations
    #check step count
    #if step count is higher than current largest, currentnum is new highest
    operations()
    currentnum -= 1
