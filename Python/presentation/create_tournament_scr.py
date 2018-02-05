import curses
from datetime import datetime

from data import database
from models.tournament_model import Tournament

def initialize(scr):
    scr.erase()
    
    curses.curs_set(1)

    curses.echo()

    scr.move(0,0)

    scr.addstr("Tournament Name: ")
    tourn_name = scr.getstr()
    scr.addstr("Number of Rounds: ")
    num_rounds = int(scr.getstr())
    scr.addstr("Length of Rounds: ")
    length = int(scr.getstr())
    scr.addstr("Start date: ")
    string_time = scr.getstr()
    type_of_string = type(string_time)

    scr.addstr(str(type))
    start_date = datetime.strptime(str(string_time), '%d/%m/%y %H:%M')

    model = Tournament(tourn_name, num_rounds, start_date, length)
    Database.save_pairing_model(model)

    scr.getch()
