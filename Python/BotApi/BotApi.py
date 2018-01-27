#!/usr/bin/python3

# Will use curses for the GUI

import curses

scr = curses.initscr()
scr.keypad(0)
curses.noecho()

scr.addstr("Hello world")
scr.refresh()
scr.getch()

curses.endwin()
