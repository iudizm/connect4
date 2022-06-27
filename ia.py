import player
import trueRandom


class Ia(player.Player):

    def __init__(self, piece="O"):
        super().__init__(piece)
        self.trueRandomPlays = trueRandom.generate()

    def makeAMove(self, game):
        print(self.trueRandomPlays)
        chosen_column = self.getRandomPlays()
        stack_index = chosen_column - 1
        if game.columns()[stack_index].isNotFull():
            game.columns()[stack_index].push(self.piece)
            game.board()[6 - len(game.columns()[stack_index])][stack_index] = game.columns()[stack_index].top()
        else:
            self.makeAMove(game)
        return game.board(), game.columns()

    def getRandomPlays(self) -> int:
        if not self.trueRandomPlays:
            self.trueRandomPlays = trueRandom.generate()
        return self.trueRandomPlays.pop()
