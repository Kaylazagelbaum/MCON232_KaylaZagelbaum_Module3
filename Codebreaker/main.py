# import classes
from classes import Player
from classes import Code
from classes import Evaluator
from classes import Game

# create objects from classes
player = Player()
code = Code()
evaluator = Evaluator()
game = Game(code, player, evaluator)

# Generate a secret code
secret_code = code.generate_code()


# prompt the user for guesses
# evaluate each guess
# display feedback after each attempt
# end when:
    # the player guesses correctly
    # attempts run out
game.play()

