#Problem 16
#2tothefifteenth = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

#What is the sum of the digits of the number 2totheonethousandth?

#Find two to the 1000th

#print the value of 2^1000, add the individual digits of it
#  For each digit of the string, add it to a variable. Then, increment to the
#  next digit in the string.


test = long(2**25)
total = 0

print test
print range(test)

for item in range(test):
    print "\n"
    print item
    total += item
    print "Total: "
    print total

#for character in test:
 #   print character
  #  total = total + character
   # print "Total: "
    #print total

#for each digit in 2**1000, print it out individually

#print str(2**1000)

#print len(str(2**1000))

#value = 2**1000

#[3*x for x in value]
