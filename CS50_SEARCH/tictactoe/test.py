from tictactoe import *

board_1 = initial_state()
board_2 = [[O, EMPTY, O],
            [EMPTY, O, X],
            [EMPTY, X, O]]


print(utility(board_2))