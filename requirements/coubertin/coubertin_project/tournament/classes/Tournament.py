class Tournament:
    def __init__(self, name, nbPlayers):
        self.nbPlayers = nbPlayers
        self.name = name
        self.state = 0 # 0 = inscritpion, 1 = en cours, 2 = termine
        self.onGoingGames = 0
        self.players = []
        self.gameHistory = [] # Liste des dictionnaires de games

    def addPlayer(self, player):
        self.players += player

    def addGame(self, game):
        pass
                
tournaments = {}
