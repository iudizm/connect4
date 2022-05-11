import player
from random import randint

class Ia(player.Player):
    
    def __init__(self, piece="🤖"):
        super().__init__(piece)


    def makeAMove(self, game):
        chosen_column = randint(1, 7)
        stack_index = chosen_column - 1
        
        if game.columns()[stack_index].isNotFull():
            game.columns()[stack_index].push(self.piece)
            game.board()[6 - len(game.columns()[stack_index])][stack_index] = game.columns()[stack_index].top()
        else:
            self.makeAMove(game)
        return game.board(), game.columns()
