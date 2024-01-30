class Player:
    def __init__(self, name):
        self.name = name
        self.victories = 0
        self.defeats = 0
    def gameLost(self):
        self.victories += 1
    def gameWon(self):
        self.victories += 1

class Match:
    def __init__(self, players):
        self.players = players
        
class Tournament:
    def __init__(self, name, maxPlayers, password):
        self.players = []
        self.name = name
        self.maxPlayers = maxPlayers
        self.password = password
    def addPlayer(self, player):
        self.players.append(player)
    # start date, ... ?
    