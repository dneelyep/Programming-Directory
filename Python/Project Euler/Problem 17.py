#Problem 17
#If the numbers 1 to 5 are written out in words: one, two, three, four, five,
#then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
#words, how many letters would be used?

#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two)
#contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of
#"and" when writing out numbers is in compliance with British usage.

totalletters = 0
currentnumber = 1

while currentnumber < 1001:
    if len(str(currentnumber)) == 1:
        if currentnumber == 1:
            print "One"
        elif currentnumber == 2:
            print "Two"
        elif currentnumber == 3:
            print "Three"
        elif currentnumber == 4:
            print "Four"
        elif currentnumber == 5:
            print "Five"
        elif currentnumber == 6:
            print "Six"
        elif currentnumber == 7:
            print "Seven"
        elif currentnumber == 8:
            print "Eight"
        elif currentnumber == 9:
            print "Nine"
    elif len(str(currentnumber)) == 2:
        #FIRST DIGIT INSTRUCTIONS:
        #if value of first digit = x: print blah
        #print str(currentnumber)[:]
        
        #SECOND DIGIT INSTRUCTIONS:
        #if value of second digit = y: print blah
        print "2 Digits"
    elif len(str(currentnumber)) == 3:
        #FIRST DIGIT INSTRUCTIONS:
        #ADD 7 DIGITS FOR HUNDRED
        #ADD 3 DIGITS FOR AND
        #SECOND DIGIT INSTRUCTIONS:
        #THIRD DIGIT INSTRUCTIONS:
        #print 2 numbers to test, then 3
        currentnumber[0:2]
        print "3 Digits"
    else:
        print "4 Digits"
    currentnumber += 1

#So:

#Split the value of currentnumber into individual digits.
    #Set a series of if statements: if digit = 1, add 3 to totalletters, etc.
        #This should set the values of individual digits in numbers to correct values, IE: 3 for '1', 5 for '8'.
        #Then, for all the numbers 1-1000, take the new values of digits and add them to a variable, print the variable.
        #Increment currentnumber until it reaches 1000


#  one   = 3
#  two   = 3
#  three = 5
#  four  = 4
#  five  = 4
#  six   = 3
#  seven = 5
#  eight = 5
#  nine  = 4
#  ten   = 3

#  eleven    = 6
#  twelve    = 6
#  thirteen  = 8
#  fourteen  = 8
#  fifteen   = 7
#  sixteen   = 6
#  seventeen = 9
#  eighteen  = 8
#  nineteen  = 8

#  twenty  = 6
#  thirty  = 6
#  forty   = 5
#  fifty   = 5
#  sixty   = 5
#  seventy = 7
#  eighty  = 6
#  ninety  = 6

#  hundred = 7
#  and     = 3
