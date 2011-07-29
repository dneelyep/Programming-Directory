#Problem 5
#2520 is the smallest number that can be divided by each of the numbers
#from 1 to 10 without any remainder.

#What is the smallest number that is evenly divisible by all of the
#numbers from 1 to 20?




#currentnumber - holds the value of the variable being tested
#To solve problem:
#For currentnumber:
#1. see if currentnumber % 1 = 0, if so, then % 2 = 0, ..., then % 20 = 0
#2. if any of the above do not result in % 0, currentnumber=currentnumber + 1
#3. if all of the above work, print currentnumber

currentnumber = 2

while currentnumber < 500000000:
    if currentnumber % 11 == 0 and currentnumber % 12 == 0 and currentnumber % 13 == 0 and currentnumber % 14 == 0 and currentnumber % 15 == 0 and currentnumber % 16 == 0 and currentnumber % 17 == 0 and currentnumber % 18 == 0 and currentnumber % 19 == 0 and currentnumber % 20 == 0:
        print currentnumber
    currentnumber += 2

#1-20 number relationships:
        #11
        #12
        #13
        #14 (2, 7)
        #15 - 5, 0
        #16 (2, 8)
        #17
        #18 (2, 3, 6, 9)
        #19
        #20 (1, 2 4, 5, 10)
        #Solution can't end in an odd number, due to even numbers
        #Solution has to end in a 0, due to multiples of 15 and 20
