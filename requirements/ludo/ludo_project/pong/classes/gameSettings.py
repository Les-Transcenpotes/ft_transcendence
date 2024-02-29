class gameSettings:
    def __init__(self, screenHeight, screenWidth, playerHeight, playerWidth, ballSize):
        self.screenHeight = screenHeight
        self.screenWidth = screenWidth
        self.playerHeight = playerHeight
        self.playerWidth = playerWidth
        self.ballSize = ballSize
        print("gameSettings are:")
        print("screenHeight: " + str(self.screenHeight))
        print("screenWidth: " + str(self.screenWidth))
        print("playerHeight: " + str(self.playerHeight))
        print("playerWidth: " + str(self.playerWidth))
        print("ballSize: " + str(self.ballSize))