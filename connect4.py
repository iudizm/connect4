import player

class Connect4():
    def __init__(self):
        self.__gameEntities = self.initializeGameEntities()

    def initializeGameEntities():
        gameEntities = [player.Player("joao"), player.Player("maria")]
        return gameEntities

    def start(self):
        self.initializeGameEntities()
        while True:
            pass