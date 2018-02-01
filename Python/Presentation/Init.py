#!/usr/bin/python3

# Will use curses for the GUI

import curses
import tournament

def initialize():
    scr = curses.initscr()
    try:
        #print("Creating screen")
        if scr is None:
            scr.addstr("\nScr is null")
        scr.addstr("\nSet keypad 0")
        scr.keypad(0)
        scr.addstr("\nSet scrollok 1")
        scr.scrollok(1)
        scr.addstr("\nSet timeout 1")
        scr.timeout(-1)
        scr.addstr("\nnoecho")
        curses.noecho()

        scr.addstr("\nAbout to initialize tournament")
        tournament.initialize(scr)
        #curses.endwin()

    except Exception as ex:
        scr.addstr("\nAn error happened")  
        print (ex)
        
    except:
        scr.addstr("\nAn error occured")
    finally:
        scr.addstr("\nEnding window")
        #curses.endwin()
        scr.addstr("\nWindow closed")

initialize()
