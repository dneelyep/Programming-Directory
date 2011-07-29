# quitgame.py : Contains the quitgame() function, used, obviously, to quit the game.
import main

def quitgame():
    print "\nWould you like to >>>close<<< the game completely, or return to the main >>>menu<<< ?"
    main.inputprompt()
    if playerinput == 'close':
        print "Game closing nao."
#        MAKE THIS ACTUALLY CLOSE THE GAME
    elif playerinput == 'menu':
        menu()
    else:
        print "\nYou entered something incorrectly. Please try again."
