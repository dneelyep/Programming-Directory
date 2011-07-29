#So I need to draw a map. Depending on characteristics of each cell in the map, the cell's appearance changes.
#These characteristics are:
#    * content  - what the cell displays when revealed.
#    * revealed - if true, the cell's 'content'' is revealed. If not, the content remains hidden.
#    * walkedon - if true, the cell displays the character. If not, displays the normal appearance. Also, switches back to normal appearance when the character exits the cell.

#So I want x number of rows to be drawn, with each cell in the row drawn differently according to its properties.
#  How do properties get determined? They're all set at certain values when the map loads.

def map():
#    class map:

    class cell:
        revealed = 0
        walkedon = 0

    def checkproperties():
        if cell.revealed == 0:
            print "[]"
        elif cell.revealed == 1:
            print "Cellcontenthere."

    checkproperties()
    generaterow()


def generaterow():
# Generates a row of cells, each with properties initialized to 0

map()


So I can represent rows by lists of instances of a cell class.


## A blank map:

##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]


## A blank map, with character in the top-left space

##[*][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]


## A partially-revealed map - x's represent areas that can't be navigated to

##| |xxx[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##| |xxx[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##| |xxx[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##| |xxx[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##|_____  |[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ]|*|[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]
##[ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ][ ]


## A filled-in map

##| |xxxxxx _ xxxxxxxxxxxxxxxxxxxxx|  ___   ____________     |
##| |xxxxxx| |xxx _ xxxxxxxxxxxxxxx| |xxx|_|xxxxxxxxxxxx|    |
##| |xxxxxx| |xxx| |xxxxxxxxxxxxxxx| |_____ xxxxxxxxxxxx|    |
##| |xxxxxx| |xxx| |_____ xxxxxxxxx|_____  |xxxxxxxxxxxx|    |
##|________  |xxx|_____  |xxxxxxxxxxxxxxx| |xxxxxxxxxxxx|    |
##xxxxxxxxx| |xxxxxxxxx| |xxxxxxxxxxxxxxx| |xxxxxx _____|    |
##xxxxxxxxx| |_________| |xxxxxxxxxxxxxxx| |xxxxxx|          |
##xxxxxxxxx|  ___________|xxxxxxxxxxxxxxx| |xxxxxx|  ______  |
##xxxxxxxxx| |xxxxxxxxxxxx ______________| |xxxxxx| |xxxxxx| |
##xxxxxxxxx| |xxxxxxxxxxxx|  ______________|xxxxxx| |xxxxxx| |
##xxxxxxxxx| |____________| |xxxxxxxxxxxxxxxxxxxxx| |xxxxxx| |
##xxxxxxxxx|  ____________  |xxxxxxxxxxxx ________| |xxxxxx| |
##xxxxxxxxx| |xxx _ xxxxxx| |xxxxxxxxxxxx|  ________|xxxxxx| |
##xxxxxxxxx| |xxx| |xxxxxx| |xxxxxxxxxxxx| |xxx _ xxxxxxxxx| |
##xxxxxxxxx| |xxx| |______| |xxxxxxxxxxxx| |___| |xxxxxxxxx| |
##xxx _____| |xxx|__________|xxxxxxxxxxxx|_______|xxx _____| |
##xxx|   ____|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|  ___  |
##xxx|  |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |___| |
##xxx|__|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|_____  |
##xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |


## A filled-in map, with extra goodies: T = Treasure, B = Boss

##| |xxxxxx _ xxxxxxxxxxxxxxxxxxxxx|  ___   ____________     |
##| |xxxxxx|T|xxx _ xxxxxxxxxxxxxxx| |xxx|_|xxxxxxxxxxxx|    |
##| |xxxxxx| |xxx| |xxxxxxxxxxxxxxx| |_____ xxxxxxxxxxxx|    |
##| |xxxxxx| |xxx| |_____ xxxxxxxxx|_____  |xxxxxxxxxxxx|    |
##|________  |xxx|_____  |xxxxxxxxxxxxxxx| |xxxxxxxxxxxx|    |
##xxxxxxxxx| |xxxxxxxxx| |xxxxxxxxxxxxxxx| |xxxxxx _____|    |
##xxxxxxxxx| |_________| |xxxxxxxxxxxxxxx| |xxxxxx|          |
##xxxxxxxxx|  ___________|xxxxxxxxxxxxxxx| |xxxxxx|  ______  |
##xxxxxxxxx| |xxxxxxxxxxxx ______________| |xxxxxx| |xxxxxx| |
##xxxxxxxxx| |xxxxxxxxxxxx|  ______________|xxxxxx| |xxxxxx| |
##xxxxxxxxx| |____________| |xxxxxxxxxxxxxxxxxxxxx| |xxxxxx| |
##xxxxxxxxx|  ____________  |xxxxxxxxxxxx ________| |xxxxxx| |
##xxxxxxxxx| |xxx _ xxxxxx| |xxxxxxxxxxxx|  ________|xxxxxx| |
##xxxxxxxxx| |xxx| |xxxxxx| |xxxxxxxxxxxx| |xxx _ xxxxxxxxx| |
##xxxxxxxxx| |xxx| |______| |xxxxxxxxxxxx| |___|B|xxxxxxxxx| |
##xxx _____| |xxx|__________|xxxxxxxxxxxx|_______|xxx _____| |
##xxx|   ____|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|  ___  |
##xxx|  |xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|T|___| |
##xxx|__|xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx|_____  |
##xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx| |
