def enterPlayer(twitchName, lichessName):
   player = Player(0, twitchName, lichessName, 1500) 
   Database.saveFunction(player)

print("Hello world")
