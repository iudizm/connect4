from stack import Stack
from player import Player
from ia import Ia

class Connect4():

    def __init__(self):
        self.__board = self.initializeBoard()
        self.__stacks = self.initializeStacks()

    def initializeBoard(self):
        rows = ['a', 'b', 'c', 'd', 'e', 'f']
        board = []
        for i in range(0, len(rows)):
            board.append([' '] * 7)
        return board

    def initializeStacks(self):
        stacks = [Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack()]
        return stacks

    def showBoard(self, board):
        rows = ['a', 'b', 'c', 'd', 'e', 'f']
        top = '    1   2   3   4   5   6   7   '
        row = [[n] for n in range(0, 7)]
        row[0][0] = 'f | '
        row[1][0] = 'e | '
        row[2][0] = 'd | '
        row[3][0] = 'c | '
        row[4][0] = 'b | '
        row[5][0] = 'a | '
        print('')
        print('  ' + '-' * (len(top) - 3))
        for j in range(0, len(rows)):
            for i in range(1, 8):
                row[j][0] = row[j][0] + str(board[j][i - 1]) + ' | '
            print(row[j][0])
            print('  ' + '-' * ((len(row[j][0]) - 3)))
        print(top)
        print('')

    def checkWin(self, S, board):
        game = False
        # Horizontal checker
        for j in range(0, 6):
            for i in range(3, 7):
                if (board[j][i]==board[j][i-1]==\
                    board[j][i-2]==board[j][i-3]==S):
                    game = True
                else:
                    continue
        # Vertical checker
        for i in range(0, 7):
            for j in range(3, 6):
                if (board[j][i]==board[j-1][i]==\
                    board[j-2][i]==board[j-3][i]==S):
                    game = True
                else:
                    continue
        # Diagonal checker
        for i in range(0, 4):
            for j in range(0, 3):
                if (board[j][i]==board[j+1][i+1]==\
                    board[j+2][i+2]==board[j+3][i+3]==S or
                    board[j+3][i]==board[j+2][i+1]==\
                    board[j+1][i+2]==board[j][i+3]==S):
                    game = True
                else:
                    continue
        if game == True:
            print(S + ' wins!')
        return game

    def instructions(self):
        return ('To play: enter an integer between 1 to 7 ' + \
            'corresponding to each column in the board. ' + \
            'Whoever stacks 4 pieces next to each other, ' + \
            'either horizontally, vertically or diagonally wins.')

    def start(self):
        self.showBoard(self.__board)
        print(self.instructions())
        player = Player()
        ia = Ia()
        
        while True:
            # X player
            self.__board, self.__stacks = player.move('X', self.__board, self.__stacks, player.piece())
            self.showBoard(self.__board)
            
            if self.checkWin(player.piece(), self.__board):
                break
            
            # O player
            self.__board, self.__stacks = ia.move('O', self.__board, self.__stacks, ia.piece())
            self.showBoard(self.__board)
            if self.checkWin(ia.piece(), self.__board):
                break
        print('Good game.')
