#Problem 9
#A Pythagorean triplet is a set of three natural
# numbers, a  < b  < c, for which, a^2 + b^2 = c^2

#For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

#There exists exactly one Pythagorean triplet for which a + b + c = 1000.
#Find the product abc.

#So: using variables a, b, and c. Find combinations of a^2 and b^2 that equal c^2
#  first, stopping a and b at like 1000. Then, review all combinations, see which
#  product = 1000

# c*c = a*a + b*b

a = 1
b = 2

while b < 1001:
    print (a*a) + (b*b)
    a += 1
    b += 1
