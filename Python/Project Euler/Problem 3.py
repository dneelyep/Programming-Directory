#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?


#A prime number is a number which is only divisible by 1 and itself
#    so you can only divide a prime number by 1 and itself, no other numbers are possible


#and a prime factor is just a prime number that factors into another number, evenly

#    in other words a prime factor is a prime number which another number can be divided by with no remainder
#        so if x is a prime number, x is ALSO a prime factor IF another number can be divided by x with no remainder
#        IE: if y/x produces a remainder of 0, that makes x a prime factor of y

#This also implies that there are a limited number of possible prime factors for any given number, since it is impossible to divide a number by more than itself evenly



#Check if the current number is a factor of <INPUT>
#    if so:
#        Add the current number to a list or something, then repeat the above step, but checking against the number the old one multiplied by to get <INPUT>
#    if it IS NOT:
#        Move on to the next number



# mainnum - the main number to check for factors
# findfactor() - finds the largest factor of a given number

def findfactor():
    # setting it to 2 because setting it to 1 would set factors as 1 and mainnum each time
    checkingnum = 2
    mainnum = 600851475143

    while checkingnum < mainnum:
        if mainnum % checkingnum == 0:
            print checkingnum, mainnum / checkingnum
            mainnum = mainnum / checkingnum
        checkingnum += 1

findfactor()

#Brute force:


#    Check whether or not the current number is a prime
#        if it IS:
#            Check if it is a factor of 600851475143
#            
#        if it IS NOT:
#            Move on to the next number



#BETTER STRATEGY:
   
#    Find all the factors of 600851475143
#        
#    See which is the largest prime


#    start at the top, count down to save time?
