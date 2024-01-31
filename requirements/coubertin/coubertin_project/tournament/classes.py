class Match:
    def __init__(self, players, round):
        self.players = players
        self.score = [0, 0] # In the same order than players ?
        self.round = round

class Player:
    def __init__(self, id):
        self.id = id
        self.matches = []
    def addMatch(self, match):
        self.matches.append(match)
  
class Tournament:
    def __init__(self, name, creator, maxPlayers, password):
        self.players = []
        self.name = name
        self.creator = creator
        self.maxPlayers = maxPlayers
        self.password = password
    def addPlayer(self, playerId):
        self.players.append(playerId)
    # start date, ... ?
    