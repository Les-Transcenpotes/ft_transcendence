class Tournament:
    def __init__(self, name, nbPlayers):
        self.nbPlayers = nbPlayers
        self.name = name
        self.state = 0 # 0 = inscritpion, 1 = en cours, 2 = termine
        self.onGoingGames = 0
        self.players = []
        self.gameHistory = []

    def addPlayer(self, player):
        self.players += player

    def startTournament(self):
        self.state += 1
        while (self.state < 2):
            self.startRound()
            while (self.onGoingGames): # Mieux a faire ?
                pass

    def startRound(self):
        i = 0
        self.onGoingGames = 0
        while (i < len(self.players)):
            # start game avec self.players[i] et self.players[i + 1] --> poster au matchmaking
            i += 2
            self.onGoingGames += 1

    def addGame(self, game): # pas pour la db, ludo va le faire ! game est un dictionnaire !
        self.gameHistory += game
        for player in game:
            if (game[player] < 5):
                self.players.remove(player)
        # Enlever le player qui a perdu dans self.players
                
tournaments = {}
