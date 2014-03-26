from term2048.board import Board
from term2048.game import Game

game = Game()
score = game.loopAI()
won = game.board.won()
print score
