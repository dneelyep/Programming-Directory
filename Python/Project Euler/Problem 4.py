#A palindromic number reads the same both ways. The largest palindrome
#made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

#So: for all numbers 100-999:
#

# So number is the input palindrome
# counter is used to run the function on multiple input values

counter = 0

def is_palindrome(number):
    """
    Checks to see if the input is or is not a palindrome.
    """

    left_num = 0
    right_num = -1
    if number[left_num] == number[right_num]:
        if can_go_in_more:
        #    Start over.
            left_num += 1
            right_num -= 1
        else:
            print number + "is a palindrome."
            #Start next number
    else:
        print number + " is not a palindrome."
        #Start next number

def find_middle(number):

    length = len(str(number))

    if length % 2 == 0:
        # If the input is even
        print "It will take " + str(length / 2) + " steps for " + str(number) + " to be solved for."
    else:
        print "It will take " + str(length / 2) + " steps for " + str(number) + " to be solved for, NOT including the step to print the middle."

my_input = 1234567

find_middle(my_input)



#Idea: find the len() of the input.
#From that, compute the middle depending on if it's even or odd.
#Do the steps the amount of times that will result in a correct answer.
