import curses
from datetime import datetime

from data import database
from models.tournament_model import Tournament

def initialize(scr):
    scr.erase()
    
    curses.curs_set(1)

    #Let the user see what they are typing
    curses.echo()

    scr.move(0,0)

    scr.addstr("Tournament Name: \n")
    #tourn_name = scr.getstr()
    scr.addstr("Number of Rounds: \n")
    #num_rounds = int(scr.getstr())
    scr.addstr("Length of Rounds: \n")
    # length = int(scr.getstr())
    scr.addstr("Start date: \n")

    scr.insch(3, 14, ' ', curses.A_REVERSE)
    scr.insch(3, 15, ' ', curses.A_REVERSE)
    scr.insch(3, 16, '/')
    scr.insch(3, 17, ' ', curses.A_REVERSE)
    scr.insch(3, 18, ' ', curses.A_REVERSE)
    scr.insch(3, 19, '/')
    scr.insch(3, 20, ' ', curses.A_REVERSE)
    scr.insch(3, 21, ' ', curses.A_REVERSE)
    scr.insch(3, 22, ' ')
    scr.insch(3, 23, ' ', curses.A_REVERSE)
    scr.insch(3, 24, ' ', curses.A_REVERSE)
    scr.insch(3, 25, ':')
    scr.insch(3, 26, ' ', curses.A_REVERSE)
    scr.insch(3, 27, ' ', curses.A_REVERSE)

    scr.move(0,17)
    tourn_name = scr.getstr()

    scr.move(1,18)
    num_rounds = int(scr.getstr())

    scr.move(2,18)
    length = int(scr.getstr())

    scr.move(3,14)
    utf_date_string = str(scr.getstr(), 'utf-8')

    #21/11/06 16:30
    start_date = datetime.strptime(utf_date_string, '%d/%m/%y %H:%M')

    model = Tournament(tourn_name, num_rounds, start_date, length)
    database.save_pairing_model(model)

    scr.getch()
