import curses

# http://www.codehaven.co.uk/using-arrow-keys-with-inputs-python/
# https://stackoverflow.com/questions/32252733/interpreting-enter-keypress-in-stdscr-curses-module-in-python
# https://stackoverflow.com/questions/6807808/highlighting-and-selecting-text-with-python-curses
def initialize(scr):
    scr.erase()
    scr.move(0,0)
    scr.addstr("1. Create Tournament\n")
    scr.addstr("2. Load Tournament\n")
    line_hilighted = 0
    scr.chgat(line_hilighted , 0, curses.A_REVERSE)
    # make cursor invisible
    curses.curs_set(0)
    while True:
        direction = scr.getch()
        if direction  == curses.KEY_DOWN:
            if(line_hilighted != 1):
                scr.chgat(line_hilighted, 0, curses.A_NORMAL)
                line_hilighted   =  line_hilighted + 1
                scr.chgat(line_hilighted , 0, curses.A_REVERSE)
        elif direction  == curses.KEY_UP:
            if(line_hilighted != 0):
                scr.chgat(line_hilighted, 0, curses.A_NORMAL)
                line_hilighted  =  line_hilighted - 1
                scr.chgat(line_hilighted , 0, curses.A_REVERSE)
        elif direction == curses.KEY_ENTER or direction == 10 or direction == 13:
            break;
