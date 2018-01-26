
def createTournament(start, howManyRounds, roundDuration):
    i = 0
    roundStart = start
    rounds = []
    while i < howManyRounds:
       i = i + 1 
       endOfRound = roundStart + roundDuration
       round = Round([], startDate, endOfRound) 
       rounds.add(round)

    tournament = Tournament(rounds, [], start)
    return tournament

def addPlayerTournament(player):
   players.add(player) 

def createNewRound(tournament):
    round = Round.createRound(
