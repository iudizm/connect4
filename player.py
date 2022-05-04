from random import randint

class Player():
	
	def __init__(self, piece_type="X"):
		self.piece_type = piece_type

	def wins(self):
		return "Player %s wins the game!"%(self.piece_type)
	
	def makeAMove(self):
		pass

	def piece(self):
		return self.piece_type
		
	def move(self, board, Stacks):
		Set0 = {'1','2','3','4','5','6','7'}
		if self.piece() == "🤖":
			pos = randint(1, 7)
			if len(Stacks[pos - 1]) < 6:
				Stacks[pos - 1].push(self.piece())
				board[6-len(Stacks[pos-1])][pos-1] = \
				Stacks[pos-1].peek()
			else:
				self.move(board, Stacks)
		else:
			pos = str(input('Your move: '))
			if (pos in Set0) == False:
				print('Input must be integer between 1 and 7')
				self.move(board, Stacks)
			else:
				pos = int(pos)
				if len(Stacks[pos - 1]) < 6:
					Stacks[pos - 1].push(self.piece())
					board[6-len(Stacks[pos-1])][pos-1] = \
						Stacks[pos-1].peek()
				else:
					print('Column full, try again...')
					self.move(board, Stacks)
		return board, Stacks
