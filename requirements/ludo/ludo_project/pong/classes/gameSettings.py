class gameSettings:
    def __init__(self):
        self.screenHeight = 1080
        self.screenWidth = 1920
        self.playerHeight = self.screenHeight / 6
        self.playerWidth = self.screenWidth / 120
        self.ballSize = self.screenWidth / 100
        print("gameSettings are:")
        print("screenHeight: " + str(self.screenHeight))
        print("screenWidth: " + str(self.screenWidth))
        print("playerHeight: " + str(self.playerHeight))
        print("playerWidth: " + str(self.playerWidth))
        print("ballSize: " + str(self.ballSize))