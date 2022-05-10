import player
from random import randint

class Ia(player.Player):
    
    def __init__(self, piece="🤖"):
        super().__init__(piece)


    def makeAMove(self, board, stacks):
        chosen_column = randint(1, 7)
        stack_index = chosen_column - 1
        
        if stacks[stack_index].isNotFull():
            stacks[stack_index].push(self.piece)
            board[6 - len(stacks[stack_index])][stack_index] = stacks[stack_index].top()
        else:
            self.makeAMove(board, stacks)
        return board, stacks
