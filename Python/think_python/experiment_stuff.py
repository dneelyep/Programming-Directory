#Exercise 3.3 Python provides a built-in function called len that returns the length of a string, so the value of len('allen') is 5.
#Write a function named right_justify that takes a string named s as a parameter and prints the
#string with enough leading spaces so that the last letter of the string is in column 70 of the display.

def right_justify(s):
    """
    Aligns input text such that the last character of input text sits in the 70th column.
    """
    print " " * (70-len(s)) + s




#Exercise 3.4 A function object is a value you can assign to a variable or pass as an argument. For
#example, do_twice is a function that takes a function object as an argument and calls it twice:
def do_twice(f, v):
    f(v)
    f(v)

def do_four(g, w):
    do_twice(g, w)
    do_twice(g, w)
    
def print_twice(string):
    print string * 2

def draw_row():
    print "+ - - - - + - - - - +"

def draw_top_box():
    print "+ - - - - + - - - - +"
    print "|         |         |"
    print "|         |         |"
    print "|         |         |"
    print "|         |         |"

def draw_two_cols():
    print "+ - - - - + - - - - + - - - - + - - - - +"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "+ - - - - + - - - - + - - - - + - - - - +"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "+ - - - - + - - - - + - - - - + - - - - +"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "+ - - - - + - - - - + - - - - + - - - - +"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "|         |         |         |         |"
    print "+ - - - - + - - - - + - - - - + - - - - +"

def draw_grid(grid_size):
    if grid_size == 1:
        draw_top_box()
        draw_top_box()
        draw_row()
    else:
        draw_two_cols()

def draw_better_grid(size):
    short_break = "+ - - - - " * size + "+\n"
    short_row   = "|         " * size + "|"
    box_rows    = short_row + "\n" + short_row + "\n" + short_row + "\n" + short_row
    three_rows = short_break + box_rows
    print three_rows,
    print three_rows
    print three_rows

draw_better_grid(3)

#Hint: to print more than one value on a line, you can print a comma-separated sequence:
#print '+', '-'
#If the sequence ends with a comma, Python leaves the line unfinished, so the value printed next appears on the same line.
#print '+',
#print '-'
#The output of these statements is '+ -'.

#A print statement all by itself ends the current line and goes to the next line.
#
#2. Use the previous function to draw a similar grid with four rows and four columns.
