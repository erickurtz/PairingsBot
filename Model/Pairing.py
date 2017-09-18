class Pairing:

    def __init__(self, playerOne, playerTwo, result, pairId):

        p1WhiteRatio = float playerOne.numWhites/playerOne.numGames
        p2WhiteRatio = float playerTwo.numwhites/playerTwo.numGames

        if(p1WhiteRatio < p2WhiteRatio):
            self.playerWhite = playerOne
            self.playerBlack = playerTwo
        elif(p1WhiteRatio > p2Whiteratio):
            self.playerWhite = playerTwo
            self.playerBlack = playerOne
        elif(playerOne.rating < playerTwo.rating):
            self.playerWhite = playerOne
            self.playerBlack = playerTwo
        else:
            self.playerWhite = playerTwo
            self.playerBlack = playerOne
            
            #maybe random? 
