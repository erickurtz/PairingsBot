import curses

def initialize(scr):
    scr.addstr("\nIn tournament")
    scr.addstr("\nCreate Tournament!\n")
    scr.refresh()
    choice = scr.getkey()
    if choice == 'c' or choice == 'C':
        scr.addstr("\nNice!")
        scr.getkey()

