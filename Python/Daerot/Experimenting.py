#figuring out how to work the app
def newbook():
    booktitleinput = raw_input("What is the title of the book? ")
    bookauthorinput = raw_input("Who is the author(s) of the book? ")
    bookyearinput = raw_input("What year was the book published? ")
    print 'Book Title: ' + booktitleinput
    print 'Author(s): ' + bookauthorinput
    print 'Year: ' + bookyearinput + '\n'
    introtext()

def introtext():
    print 'Welcome to Daerot,  a simple program designed to let you have an easily'
    print 'configurable to-do list for reading.\n'
    print 'To get started adding your first book to the list, type "addbook". From there'
    print 'you will be prompted for the required information to get on your way. Enjoy!'
    userinput = raw_input("Please enter a command: ")
    if userinput == "addbook":
        newbook()
    else:
        print 'You must have entered an incorrect command. Please try again.'
        introtext()
        
introtext()
