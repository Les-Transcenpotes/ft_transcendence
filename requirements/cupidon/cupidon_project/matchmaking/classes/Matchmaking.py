class Matchmaking():

    def __init__(self):
        self.waitingList = [] # Waiting players
        self.inGame = {} # Games: key = roomName, Value = [player1, player2]


matchmaking = Matchmaking()
