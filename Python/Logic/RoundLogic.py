def createRound(startDate, endDate, players):
    pairings = makePairings(players)
    round = Round(startDate, endDate, pairings)
    return round

def makePairings(playerList):
    self.pairingList = makePairingsHelper(playerList)
    
def makePairingsHelper(players, currentPairings):
    
    if not players:
        return currentPairings
    
    player1 = players.pop[0]
    previousPlayed = player1.previousPlayerList
    filteredPlayers = [player for player in players
                       if not in previousPlayed]
    if not players:
        return currentPairings
    
    if not filteredPlayers:
        currentPairings.append(Pairing.Pairing(player1, players.pop[0]))
        return makePairingsHelper(players, currentPairings)
    else:
        player2 = filteredPlayers.pop[0]
        players.remove(player2)
        return makePairingsHelper(players,currentPairings.append
                           (Pairing.Pairing(player1, player2)))
