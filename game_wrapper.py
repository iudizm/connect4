from connect4 import Connect4

class GameWrapper():

    def __init__(self, game = Connect4()):
        self.game = game
    
    def playAgain(self):
        i = input("Play again?\n(y/n)>>").lower()
        if i not in ('y', 'n'):
            self.playAgain()
        if i == 'n': return False
        if i == 'y': return self.newConnect4Game()

    def newConnect4Game(self):
        self.game = Connect4()
        return True

    def run(self):
        self.game.match()
        if self.playAgain():
            self.run()
        print("\n"*20)

game = GameWrapper()
game.run()
