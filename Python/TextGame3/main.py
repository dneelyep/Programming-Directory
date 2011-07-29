import prettytext
import helpmenu

def inputprompt():
    global pinput
    pinput = raw_input("\nPlease enter your choice: ")

def stats():
    #- Display player stats in a fixed box at the bottom of the screen, have them update in response to changes (real-time)
    #	- TODO: Implement bars for all stats - IE instead of just displaying 50/100 health, show a half-filled bar, maybe with 50/100 inside or beside it
    
    print "   ____________________________________                          "
    print "  /                                                              "
    print " /  ", charname
    print "|------------                                                    "
    print "|    Health:", currenthealth, "/", totalhealth
    print "|------------                                                    "
    print "|    Attack:", attack
    print "|------------                                                    "
    print "|    Experience:", experience, "/", tonextlevel
    print "|------------                                                    "
    print " \   Level:", level
    print "  \____________________________________                          "
    print "                                                                 "
    healthbar()

def healthbar():
    #Find the percentage that currenthealth/totalhealth creates
    #  - Make sure to account for rounding
    #Take that percentage and print half that many bars
    
    visualhealth = (currenthealth / totalhealth) * 100

    print visualhealth
    
    #if tensdigitetc of visualhealth >= 5:
     #   visualhealth rounds up
    #else:
        #visualhealth truncates
        
    print '-' * visualhealth

    print currenthealth, "/", totalhealth
            
    # "--------------------------------------------------"
    #  ^- 50 items

def menu():
    global pinput
    
    print "                                                                 "
    print "                      Welcome to Text Game 3!                    "
    print "                                                                 "
    print "                            'new' game                           "
    print "                              'help'                             "
    print "                              'quit'                             "
    print "                                                                 "
    print "     Note: To choose an option from the list, type the word      "
    print "                                                                 "
    print "                 indicated in quotation marks                    "
    print "                                                                 "
    print "                      and press 'enter'                          "
    
    inputprompt()
    
    if pinput == "new":
        setcharname()
    elif pinput == "help":
        helpmenu.helpmenu()
        menu()
    elif pinput == "quit":
            print "Thanks for playing. Bye now.                             "
            quit()
    else:
        print "\nYou must have entered something incorrectly. Please try    "
        print "again.                                                       "
        menu()

def setcharname():
    global charname
    
    print "\nPlease enter your character\'s name. Or, just type \'default\' "
    print "to keep the default name.                                        "
    print "\nNote: Please keep your character name to 7 characters or less. "
    inputprompt()

    if pinput == "default":
        charname = "Danyo"
    elif len(pinput) > 7:
        print "Please try again. That name is larger than 7 characters.\n   "
        setcharname()
    else:
        charname = pinput
        
    print "\n\nCongratulations, your name is", charname, "!"
    gamestarttext()

def gamestarttext():
    print "\nMan this place smells like crap. Literally. Now, where\'d those"
    print "Cheez-its go to...?                                              "
    print "                     ...                                         "
    print "                          ...and WTF is that snoring...?         "
    print "                                                                 "
    print "Meh, time to find mah Cheez-its.                                 "
    print "                                                                 "
    print "                                                                 "
    print "*Cue the Omniscient Narrator*                                    "
    print "Hello there daring young person. I gather that you\'re interested"
    print "in playing a game here and you\'re in a hurry to kill some stuff "
    print "and gain XP, amirit?                                             "
    print "                                                                 "
    print "*Ahem*. Anyways, you\'ll need to know how to play the game won\'t"
    print "you? Of course. So, let\'s get ya started.                       "
    print "                                                                 "
    print "This game\'s pretty simple. You have two main stages that you\'ll"
    print "be moving through - the Dungeon Map and Battle...thing. Excited  "
    print "now? Oh, ho, ho. I thought so.                                   "
    print "                                                                 "
    print "Anyways. To navigate the Dungeon Map, press the l, r, u, and d   "
    print "keys - for left, right, up, and down movement. Your character    "
    print "will be indicated on the map by a * symbol. That should be all   "
    print "now. If you need more help, simply type 'help' at any time.      "
    print "                                                                 "
    print "Farewell", charname, "and good luck! You\'ll need it, lest your  "
    print "brains splatter from failure. Oh, ho, ho, ho, ho, ho, ho....... "
    print "                                                                 "
    print "Wow, that guy\'s weird. Anyways, let\'s rock.                    "
    map()

def map():

    class map:
        global cellcount
        global printrow
        global printmap
        
        cellcount = 20
        
        def printrow():
            print cell.cellview * cellcount

        def printmap():
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()
            printrow()

    class cell:
        # by default, the contents of cells aren't revealed (hence, set to 0)
        # setting revealed to 1 reveals the contents of the cell
        revealed = 0

        if revealed == 0:
            cellview = "[0]"
        elif revealed == 1:
            cellview = "[1]"

    printmap()

#class cell:
 #   revealed = 0

#Map Logic
#
#  Set up the map to use arrays. Each item in each array contains a tile.
#    20 x 20 or so?
#
#  Map tiles have a 'revealed' property, set to '0' until it's been travelled over.
#
#
#
#
#
#
#
#
#
#
#
#
    print "row1"
    stats()

#def battle()


currenthealth = 10
totalhealth   = 10
attack        = 1
experience    = 0
tonextlevel   = 10
level         = 1
    
prettytext.prettytext()
menu()

#menu stuff first

#then a bit of text to introduce the story

#then the overworld screen with some text to explain movement, etc
 #   - from here, switch back and forth between exploration and the battle screen, where ya fight monsters until the game ends


#Ideas, etc:
 #Maybe put the initializing stats (where they're set before the game starts) into, say, a
 #new game function? So they're reset each time a new game starts.
 #Would make more sense mentally at least, help reduce confusion
