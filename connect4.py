from stack import Stack
from player import Player
from ia import Ia

class Connect4():

    def __init__(self):
        self.__board = self.initializeBoard()
        self.__stacks = self.initializeStacks()

    def columns(self):
        return self.__stacks

    def board(self):
        return self.__board

    def setBoard(self, board):
        self.__board = board 

    def initializeBoard(self):
        board = []
        for i in range(0, 6):
            board.append([' '] * 7)
        return board

    def initializeStacks(self):
        stacks = [Stack(), Stack(), Stack(), Stack(), Stack(), Stack(), Stack()]
        return stacks

    def showBoard(self):
        rows = ['a', 'b', 'c', 'd', 'e', 'f']
        columns = '    1   2   3   4   5   6   7   '
        row = [[n] for n in range(0, 7)]
        row[0][0] = 'f | '
        row[1][0] = 'e | '
        row[2][0] = 'd | '
        row[3][0] = 'c | '
        row[4][0] = 'b | '
        row[5][0] = 'a | '
        print('')
        print('   ' + '-' * (len(columns) - 3))
        for j in range(0, len(rows)):
            for i in range(1, 8):
                row[j][0] = row[j][0] + str(self.__board[j][i - 1]) + ' | '
            print(row[j][0])
            print('   ' + '-' * ((len(row[j][0]) - 3)))
        print(columns)
        print('')

    def checkWin(self, player):
        game_over = False
        
        # Horizontal checker
        for j in range(0, 6):
            for i in range(3, 7):
                if (self.__board[j][i] == self.__board[j][i-1] == self.__board[j][i-2] == self.__board[j][i-3] == player.piece):
                     game_over = True
                else:
                    continue
        # Vertical checker
        for i in range(0, 7):
            for j in range(3, 6):
                if (self.__board[j][i] == self.__board[j-1][i] == self.__board[j-2][i] == self.__board[j-3][i] == player.piece):
                    game_over = True
                else:
                    continue
        # Diagonal checker
        for i in range(0, 4):
            for j in range(0, 3):
                if (self.__board[j][i] == self.__board[j+1][i+1] == self.__board[j+2][i+2] == self.__board[j+3][i+3] == player.piece or
                    self.__board[j+3][i] == self.__board[j+2][i+1] == self.__board[j+1][i+2] == self.__board[j][i+3] == player.piece):
                    game_over = True
                else:
                    continue

        if game_over:
            player.wins()
        return game_over

    def instructions(self):
        return (
            '=================================================== \n' + \
            '                    HOW TO PLAY\n' + \
            '>> Enter an integer between    1   and   7\n' + \
            'corresponding to each column in the board.\n' + \
            '>> Whoever stacks 4 pieces next to each other,\n' + \
            'either horizontally, vertically or diagonally WINS!\n' + \
            '===================================================')
    
    def gameModeMenu(self):
        menu_message = (
            "\n\n" + \
            "===================================================\n" + \
            "                CHOOSE THE GAME MODE\n" + \
            "( 1 )   PLAYER vs PC \n" + \
            "( 2 )   PLAYER vs PLAYER \n" + \
            "===================================================\n('1' or '2')>>")
        r = input(menu_message)
        return r

    def definePlayers(self):
        gameMode = self.gameModeMenu()
        if gameMode == '1':
            return [Player(), Ia()]
        if gameMode == '2':
            return [Player(), Player("O")]
        self.definePlayers()

    def match(self):        
        p1, p2 = self.definePlayers()
        print(self.instructions())
        self.showBoard()       
        while True:

            # p1 turn
            self.__board, self.__stacks = p1.makeAMove(self)
            self.showBoard()

            if self.checkWin(p1):
                break
            
            # p2 turn
            self.__board, self.__stacks = p2.makeAMove(self)
            self.showBoard()
            
            if self.checkWin(p2):
                break
        
        print('Good game!')
