#Another Text Game - a bit more advanced this time

def gamemenu():
    print 'Welcome to Another Text Game. You are at the main menu.'
    print 'To view a list of commands, type "getcommands".'
    print 'To start the game, type "getstarted".'
    
    playerinput = raw_input("Please enter a command: ")
    
    if playerinput == 'getcommands':
        getcommands()
        gamemenu()
    elif playerinput == 'getstarted':
        gamestart()
    else:
        print 'You must have typed an incorrect command. Please try again.'
        gamemenu()

#getcommands - allows the player to view a list of all possible commands in the game
def getcommands():
    print '\n---Command List--- \n'

    print 'Menu Commands:\n'
    print 'getstarted - lets the player start the game from the main menu'
    print 'getcommands - lets the player view a list of all possible commands'
    print '\nGame Commands:\n'
    print 'observe - lets the player observe an object or event'
    print 'go - lets the player go to a place'
    print 'practice attack - lets the player practice their attack skill to increase it'
    print 'viewattack - lets the player view their current attack level'
    print 'attack - lets the player attack something'
    print 'NOTE: commands "observe", "go", and "attack" are to be used in combination'
    print 'with the place/event/etc they are referring to. For example, one would type'
    print '"go refrigerator" to go to the refrigerator or "observe television" to'
    print 'use the observe command on a television.\n'

gamemenu()
