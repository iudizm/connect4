from random import randint

class Player():
    
    def __init__(self, piece="😀"):
        self.piece = piece

    def wins(self):
        return "Player %s wins the game!"%(self.piece)

    def piece(self):
        return self.piece
        
    def makeAMove(self, board, stacks):
        columns = {'1','2','3','4','5','6','7'}
        chosen_column = str(input('Your move: '))
        if (chosen_column in columns) == False:
            print('Input must be an integer between 1 and 7')
            self.makeAMove(board, stacks)
        else:
            stack_index = int(chosen_column) - 1
            
            if stacks[stack_index].isNotFull():
                stacks[stack_index].push(self.piece)
                board[6 - len(stacks[stack_index])][stack_index] = stacks[stack_index].top()
            else:
                print('Column full, try again...')
                self.makeAMove(board, stacks)
        return board, stacks
