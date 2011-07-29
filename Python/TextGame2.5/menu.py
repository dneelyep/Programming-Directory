import helpstuff
import quitgame

#The main menu
def mainmenu():
    menutext = "\n=========================\nT E X T  -  G A M E  -  2.5\n=========================\n\nHello, and welcome to Text Game 2.5!\n"

    print menutext
    
    print "To start the game, type 'start'. For help, type 'help'. Or, if you're a loser, type 'quit' to leave the game."
    menuinput = raw_input('\nPlease enter your choice: ')

    if menuinput == 'start':
        setcharname()
        intro()
    elif menuinput == 'help':
        help.help()
        mainmenu()
    elif menuinput == 'status':
        print "\nYou haven't even started the game yet...\n"
        menu()
    elif menuinput == 'quit':
        quitgame.quitgame()
    else:
        print "\nYou entered something incorrectly. Please try again.\n"
        menu()
