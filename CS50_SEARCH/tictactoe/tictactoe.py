"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """

    num_moves = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] is not None:
                num_moves += 1
    # If total number of moves made is even, X's turn, else, O's turn
    if num_moves%2 == 0:
        return X
    else:
        return O

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    action = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is None:
                action.append((i,j))
    return action


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = board
    i,j = action
    if board[i][j] is not EMPTY:
        raise Exception("Not Available")
    else:
        new_board[i][j] = player(board)
    return new_board

def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Pseudocode: 
    # horizontal: write a loop that contains a variable that keeps track of just the row number. Then, define another variable, j, which represents the col num that
    #             relies on i
    # vertical: same mechanism, the difference is that it is the reverse of what horizontal does.
    # diagonal: make j same as i

        
        


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
