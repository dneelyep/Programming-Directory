#Problem 1:
#If we list all the natural numbers below 10 that are multiples of 3 or 5,
    #we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.

#So: set $currentnum = 0. For $currentnum in range 1-1000: check if
 # $currentnum % 3 = 0 and if $currentnum % 5 = 0. If yes to either of those,
  #add the value of $currentnum to the value of $threenums or $fivenums. Then
  #increment $currentnum by 1 and repeat the loop until $currentnum = 1000.
  #Add the values of $threenums and $fivenums. That should be the answer.*/

currentnum = 0
threenums  = 0
fivenums   = 0

while (currentnum < 1000):
    if currentnum % 3 == 0:
        threenums += currentnum
        currentnum += 1
        continue
    if currentnum % 5 == 0:
        fivenums += currentnum
    currentnum += 1

print threenums
print fivenums
print threenums + fivenums
