import Player.py

class Pairing:
    
    def __init__(self, whitePlayer, blackPlayer):

        self.whitePlayer = whitePlayer
        self.blackPlayer = blackPlayer
        p1WhiteRatio = float playerOne.numWhites/playerOne.numGames
        p2WhiteRatio = float playerTwo.numwhites/playerTwo.numGames

        if(p1WhiteRatio < p2WhiteRatio):
            makePairing(playerOne, playerTwo)
        elif(p1WhiteRatio > p2Whiteratio):
            makePairing(playerTwo, PlayerOne)
        elif(playerOne.rating < playerTwo.rating):
            makePairing(playerOne, playerTwo)
        else:
            makePairing(playerTwo, PlayerOne)

            #maybe random?
        self.result = null


    def makePairing(pWhite, pBlack):
         pWhite.numGames = playerOne.numGames + 1
         pWhite.numWhites = playerOne.numWhites + 1
         pBlack.numGames = playerTwo.numgames + 1
         self.playerWhite = pWhite
         self.playerBlack = pBlack
        
        
