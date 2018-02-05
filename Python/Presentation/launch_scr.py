import curses

from . import create_tournament_scr

def changeMenuItem(scr, menuLen, index):
    for i in range(0, menuLen):
        if i == index:
            scr.chgat(i, 0, curses.A_REVERSE)
        else:
            scr.chgat(i, 0, curses.A_NORMAL)


# http://www.codehaven.co.uk/using-arrow-keys-with-inputs-python/
# https://stackoverflow.com/questions/32252733/interpreting-enter-keypress-in-stdscr-curses-module-in-python
# https://stackoverflow.com/questions/6807808/highlighting-and-selecting-text-with-python-curses
def initialize(scr):
    scr.erase()
    # make cursor invisible
    curses.curs_set(0)

    #Leave echo mode. Echoing of input characters is turned off.
    curses.noecho()

    scr.move(0,0)

    menuItems = ["1. Create Tournament\n", "2. Load Tournament\n"]
    for item in menuItems:
        scr.addstr(item)

    line_hilighted = 0
    changeMenuItem(scr, len(menuItems), line_hilighted )
    while True:
        direction = scr.getch()
        if direction  == curses.KEY_DOWN:
            if(line_hilighted < len(menuItems) - 1):
                line_hilighted   =  line_hilighted + 1
                changeMenuItem(scr, len(menuItems), line_hilighted)
        elif direction  == curses.KEY_UP:
            if(line_hilighted > 0):
                line_hilighted  =  line_hilighted - 1
                changeMenuItem(scr, len(menuItems), line_hilighted)
        elif direction == curses.KEY_ENTER or direction == 10 or direction == 13:
            break

    if line_hilighted == 0:
        create_tournament_scr.initialize(scr)
