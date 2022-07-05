from random import randint

class Player():
    
    def __init__(self, piece="X"):
        self.piece = piece

    def wins(self):
        print("Player %s wins the game!"%(self.piece))
        
    def makeAMove(self, game):
        columns = ['1','2','3','4','5','6','7']
        chosen_column = str(input('"%s" move, choose a column: '%(self.piece)))
        if (chosen_column in columns) == False:
            print('Column must be an integer between 1 and 7')
            self.makeAMove(game)
        else:
            column_index = int(chosen_column) - 1
            
            if game.columns()[column_index].isNotFull():
                game.columns()[column_index].push(self.piece)
                game.board()[6 - len( game.columns()[column_index])][column_index] = game.columns()[column_index].top()
            else:
                print('Column full, try again...')
                self.makeAMove(game)
        return game.board(), game.columns()
