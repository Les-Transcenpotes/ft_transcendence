class gameSettings:
    def __init__(self):
        self.screenHeight = 1080
        self.screenWidth = 1920
        self.playerHeight = self.screenHeight / 15
        self.playerWidth = self.screenWidth / 200
        self.ballSize = self.screenWidth / 150
        print("gameSettings are:")
        print("screenHeight: " + str(self.screenHeight))
        print("screenWidth: " + str(self.screenWidth))
        print("playerHeight: " + str(self.playerHeight))
        print("playerWidth: " + str(self.playerWidth))
        print("ballSize: " + str(self.ballSize))