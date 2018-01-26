# A round is a list of pairings, and a list of players
import Player.py
import Pairing.py

class Round:
    def __init__(self, pairings, beginDate, endDate):
        self.pairingList = pairings
        self.beginDate = beginDate
        self.endDate = endDate
