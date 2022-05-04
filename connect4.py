from random import randint
from stack import Stack


class Connect4():

    def __init__(self):
        self.__board = self.initializeBoard()
        self.__stacks = self.initializeStacks()
        self.__player = "X"
        self.__ia = "O"

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

    def move(self, piece, board, Stacks, computer):
        Set0 = {'1', '2', '3', '4', '5', '6', '7'}
        if piece == computer:
            pos = randint(1, 7)
            if len(Stacks[pos - 1]) < 6:
                Stacks[pos - 1].push(piece)
                board[6-len(Stacks[pos-1])][pos-1] = \
                    Stacks[pos-1].peek()
            else:
                self.move(piece, board, Stacks, computer)
        else:
            pos = str(input('Your move: '))
            if (pos in Set0) == False:
                print('Input must be integer between 1 and 7')
                self.move(piece, board, Stacks, computer)
            else:
                pos = int(pos)
                if len(Stacks[pos - 1]) < 6:
                    Stacks[pos - 1].push(piece)
                    board[6-len(Stacks[pos-1])][pos-1] = \
                        Stacks[pos-1].peek()
                else:
                    print('Column full, try again...')
                    self.move(piece, board, Stacks, computer)
        return board, Stacks

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

    def main(self):
        self.showBoard(self.__board)
        print(self.instructions())
        game = False
        while game == False:
            # X player
            self.__board, self.__stacks = self.move('X', self.__board, self.__stacks, self.__ia)
            self.showBoard(self.__board)
            game = self.checkWin('X', self.__board)
            if game == True:
                break
            # O player
            self.__board, self.__stacks = self.move('O', self.__board, self.__stacks, self.__ia)
            self.showBoard(self.__board)
            game = self.checkWin('O', self.__board)
            if game == True:
                break
        print('Good game.')

game = Connect4()
game.main()