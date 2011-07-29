def mainmenu():
    menutext = "\n=========================\nT E X T  -  G A M E  -  2.5\n=========================\n\nHello, and welcome to Text Game 2.5!\n"
    print menutext
    print "To start the game, type 'start'. For help, type 'help'. Or, if you're a loser, type 'quit' to leave the game."
    menuinput = raw_input('\nPlease enter your choice: ')
    if menuinput == 'start':
        setcharname()
        intro()
    elif menuinput == 'help':
        help()
        mainmenu()
    elif menuinput == 'status':
        print "\nYou haven't even started the game yet...\n"
        mainmenu()
    elif menuinput == 'quit':
        quitgame()
    else:
        print "\nYou entered something incorrectly. Please try again.\n"
        mainmenu()

def quitgame():
    ''' 
    Used to quit the game.
    '''
    print "\nWould you like to >>>close<<< the game completely, or return to the main >>>menu<<< ?"
    inputprompt()
    if playerinput == 'close':
        print "Game closing nao."
    elif playerinput == 'menu':
        mainmenu()
    else:
        print "\nYou entered something incorrectly. Please try again."

def gameover():
    print "\nYou lose. Maybe you should have trained a bit more?\n"
    mainmenu()

def youwon():
    print "\nYou win! Congratulations and thanks for playing Text Game 2! It was great fun to make.\n"
    mainmenu()

def youwonlooped():
    print "\nOh wow, it looks like you found the magic loop! Remember the password \'cheez-its\' for more fun in the future... Maybe\n.\n..\n...\n....\n.....\n"

def help():
    '''
    Text to be displayed when the user asks for help
    '''
    print "\n\n=============\nH   E   L   P\n=============\n"
    print "Command List:\n-------------"
    print "* check - Usually used to check your surroundings. Combine with another parameter (for example, 'check door' or 'check fence') to check a specific item/place. \n\n* go - Go to a place. Use with a parameter to specify the place to go to ('go stairs' or 'go outside' for example) \n\n* attack - Used to attack an object/being. Use at the Training Center to practice your attack skills. \n\n* run - Used at the Training Center to increase your Health attribute. \n\n* status - Type this to view a report of your character's name and attributes. \n\n* help - Used to view the help document, containing the main Command List (You're looking at it right now).\n\n* start - Starts a new game. Only usable from the main menu.\n\n* quit - Quits the game. Loser.\n\n"

#Used for the magic loop
looped = 0
#Used to display battle initiation text with Snorlax
battlestarted = 0
snorhealth = 200
snorcurrenthealth = 200
snorattack = 3
battleround = 0

#default area text - use this when making a new area, to help keep from forgetting adding certain actions and such

#if playerinput == 'check':
#    print "TEXT HERE DEPENDING ON ENVIRONMENT
#    reenter loop
#elif playerinput == 'go':
#    print "Go where?"
#    reenter loop
#elif playerinput == 'go [+ parameter':
#    take player to place, or an error message
#    reenter loop OR function for the next area
#elif playerinput == 'attack':
#    print "TEXT HERE DEPENDING ON ENVIRONMENT"
#    reenter loop
#elif playerinput == 'run':
#    print "TEXT HERE DEPENDING ON ENVIRONMENT"
#    reenter loop
#elif playerinput == 'status':
#    status()
#    reenter loop
#elif playerinput == 'help':
#    help()
#    reenter loop
#elif playerinput == 'start':
#    print "Err...the game\'s already started..."
#    reenter loop
#elif playerinput == 'quit':
#    quitgame()
#else:
#    print "You entered something correctly. Please try again."
#    reenter loop

def setcharname():
    '''
    Used to set the name of the main character - automatically called at the beginning of a new game and can be used later to change name.
    '''
    global charname
    charname = raw_input("\nWhat would you like your character's name to be? For the default name, just enter 'default'.\n")
    if charname == 'default':
        charname = "Dudamel the Daring"

def status():
    print "Name:           ", charname
    print "Attack Rating:  ", attack
    print "Total Health:   ", health
    print "Current Health: ", currenthealth


def intro():
    '''
    Set attack, health, currenthealth attributes to default values at the start of a new game.
    '''
    global attack
    global health
    global currenthealth
    attack = 1
    health = 100
    currenthealth = 100
    
    print "\nAs the sun rises in the beautiful countryside our hero", charname,"is recovering from a wild night at the town barn. Little does he know, however, that a sneaky, slimy something is snickering and snoring as seriously as a snake. With Cheez-its in hand...\n"
    print "Welcome to Text Game 2.5! This should be a short, but hopefully interesting and...maybe?...memorable adventure.\n"
    print "First, you may want to check your surroundings. Remember, if you ever need help, simply type in 'help' to receive a list of common commands."
    home()

def home():
    inputprompt()
    if playerinput == "check":
        print "Ah, the joy of a cool Autumn evening in fields of green. Everything's perfect. Or... Wait... *", charname, "sniffs the air *\n.\n..\n...\n\"WHO...STOLE...MAH...CHEEZ-ITS?!?!?!\" roars", charname, "."
        print "As", charname, "searches the ground for hints of the beast\'s origin he comes across the smell of an ancient beast... A primordial force capable of destroying even Chuck Norris himself... The powerful... The incorruptable... The extremely lazy... "
        print "\nS \n  N \n    O \n      R \n        L \n          A \n            X\n"
        print "\"Vengeance shall be mine! This heathen shall taste the sweet kiss of mother Steele [cwutididthar] and father Death in a marvelous bloody rapture! Off to go to the Snorlax >>lair<<\""
        print "\"But wait", charname, "\" whispers the omniscient narrator, \"Don\'t you want to buff up a bit first? A Snorlax could be tough work.\""
        print "\"You\'re right Ominscient Narrator. Off first to >>train<< at the Training Center!\""
        home()
    elif playerinput == "go":
        print "\nGo where?\n"
        home()
    elif playerinput == 'go train':
        print "A Training Center...with one punching bag and a treadmill...pretentious much?"
        trainingcenter()
    elif playerinput == 'go lair' and attack != 1 and health != 100:
        print "TO DA CHOPPA...THEN DA LAIR!"
        lair()
    elif playerinput == 'go lair' and attack == 1 and health == 100:
        print "Lolz, Snorlax without training? Yea, rit."
        lair()
    elif playerinput == 'attack':
        print "...You\'re trying to destroy your home, and having visions of a Snorlax stealing your Cheez-its... You sure you took your medicine today?"
        home()
    elif playerinput == 'run':
        print charname, "scurries dutifully through the house, sniffing out any remaining crums. The Pokemon stole them all..."
        home()
    elif playerinput == 'start':
        print "Err...the game\'s already started..."
        home()
    elif playerinput == 'quit':
        quitgame()
    elif playerinput == "help":
        help()
        home()
    elif playerinput == "status":
        status()
        home()
    else:
        print "You entered something incorrectly. Please try again."
        home()

def trainingcenter():
    global attack
    global health
    global currenthealth
    global looped
    
    inputprompt()
    if playerinput == 'check':
        print "Looks like they have a punching bag to build up my Attack skill...and I can run on that treadmill to magically gain some extra Health... And wait... a magic hula >>>loop<<< in the corner... Maybe I should go to it..."
        trainingcenter()
    elif playerinput == 'go':
        print "Go where?"
        trainingcenter()
    elif playerinput == 'go home':
        print "Woo, at the cozy >>home<<stead."
        home()
    elif playerinput == 'go lair' and attack != 1 and health != 100:
        print "TO DA CHOPPA...THEN DA LAIR!"
        #MAKE SURE THIS IS WORKING CORRECTLY
        lair()
    elif playerinput == 'go lair' and attack == 1 and health == 100:
        print "Lolz, Snorlax without training? Yea, rit."
        lair()
    elif playerinput == 'attack':
        print "You attack the punching bag! Hiyah! +1 Attack skill!"
        attack += 1
        print "Attack:", attack
        trainingcenter()    
    elif playerinput == 'run':
        print "Huff! Puff! +3 Health! Yea!"
        health += 3
        currenthealth += 3
        print "Health:", health
        trainingcenter()
    elif playerinput == 'go loop' and looped == 0:
        while health and attack < 1000:
            print "IT'S A MAGIC LOOP! WOO!"
            looped = 1
            health += 10 
            attack += 10
            currenthealth += 10
            print "Magic Jump! Swoosh!"
            print "Health: ", health
            print "Attack: ", attack
        trainingcenter()
    elif playerinput == 'go loop' and looped != 0:
        print "\nSorry,", charname, "cain't jump no mo :(."
        trainingcenter()
    elif playerinput == 'status':
        status()
        trainingcenter()
    elif playerinput == 'help':
        help()
        trainingcenter()
    elif playerinput == 'start':
        print "Err...the game\'s already started..."
        trainingcenter()
    elif playerinput == 'quit':
        quitgame()
    else:
        print "You entered something incorrectly. Please try again."
        trainingcenter()

def lair():
    global battlestarted
    global battleround
    
#   IF SNORLAX IS 1-SHOTTED, SPECIAL TEXT
    inputprompt()
    
    if playerinput == 'check':
        print "Gawd it stinks in here. There\'s the biggy, Snorlax. Get ready for battle!"
        lair()
    elif playerinput == 'go':
        print "Go where? Running away? Chicken?"
        lair()
    elif playerinput == 'go home' and battlestarted == 0:
        print "Woo, at the cozy >>home<<stead."
        home()
    elif playerinput == 'go home' and battlestarted != 0:
        print "No leaving once the battle\'s already started... Hehehehehe... ATTACK OR PERISH!"
        lair()
    elif playerinput == 'go train' and battlestarted == 0:
        print "A Training Center...with one punching bag and a treadmill...pretentious much?"
        trainingcenter()
    elif playerinput == 'go train' and battlestarted != 0:
        print "No leaving once the battle\'s already started... Hehehehehe... ATTACK OR PERISH!"
        lair()
    elif playerinput == 'attack' and battlestarted == 0:
        print "LET\'S GET READY TO"
        print "R                            E"
        print "U  U                               L"
        print "M     M                         B"
        print "B        B                      M"
        print "L           L                      U"
        print "E              E   L   B   M   U   R"
        battlestarted += 1
        battleround += 1
        lair()
    elif playerinput == 'attack' and battlestarted != 0:
        attacksequence()
        lair()
    elif playerinput == 'run':
        print "Wuss. Err...oops, I mean, you can't run in this area."
        lair()
    elif playerinput == 'status':
        status()
        lair()
    elif playerinput == 'help':
        help()
        lair()
    elif playerinput == 'start':
        print "Err...the game\'s already started..."
        lair()
    elif playerinput == 'quit':
        quitgame()
    else:
        print "You entered something incorrectly. Please try again."
        lair()

def attacksequence():
    '''
    The actions to be executed during the battle scene thing
    '''
    global attack
    global health
    global currenthealth
    global snorhealth
    global snorcurrenthealth
    global snorattack
    global battleround
    
    print "You hit Snorlax for", attack, "damage"
    print "Snorlax farts on you for", snorattack, "damage"
    print "\n+++++++++++++++++++++++++++++++++++++"
    print "Round", battleround, "Results:\nSnorlax", snorcurrenthealth, "\n", charname, currenthealth
    print "+++++++++++++++++++++++++++++++++++++"
    currenthealth -= snorattack
    snorcurrenthealth -= attack
    battleround += 1
    
    if currenthealth <= 0:
        gameover()        

    if snorcurrenthealth <=0 and looped == 0:
        youwon()
    elif snorcurrenthealth <=0 and looped != 0:
        youwonlooped()

def inputprompt():
    '''
    Used as a generic input prompt - should be called everytime the game needs input from the player.
    '''
    global playerinput
    playerinput = raw_input('\nPlease enter your choice: ')

mainmenu()
