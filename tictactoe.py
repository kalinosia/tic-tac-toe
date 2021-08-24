"""
Tic Tac Toe Player
"""

import math
import random
import copy
import time

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
    # In the initial game state, X gets the first move.
    if board == initial_state(): return X

    # return which player’s turn it is (either X or O).
    howX = 0
    howO = 0

    for row in board:
        for value in row:
            if value == X:
                howX += 1
            elif value == O:
                howO += 1
            else:
                continue
    if howX > howO:
        return O
    else:
        return X
    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # function should return a set of all of the possible actions that can be taken on a given board.
    my_set = set()

    i = 0
    j = 0
    for row in board:
        for value in row:
            if value == EMPTY:  # Possible moves are any cells on the board that do not already have an X or an O in them.
                my_set.add((i, j))  # Each action should be represented as a tuple (i, j) where i corresponds to the row...
            j += 1
        i += 1
        j = 0

    return my_set
    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # should return a new board state, without modifying the original board.

    # If action is not a valid action for the board, your program should raise an exception.
    if action not in actions(board):
        raise NameError('Move not in possible moves')  # ???

    # Importantly, the original board should be left unmodified:
    # You’ll likely want to make a deep copy of the board first before making any changes.
    new_board = copy.deepcopy(board)

    # The returned board state should be the board that would result from taking the
    # original input board, and letting
    # the player whose turn it is make their move at the cell indicated by the input action.
    new_board[action[0]][action[1]] = player(board)
    return new_board

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # The winner function should accept a board as input, and return the winner of the board if there is one.
    # have_winner = False

    if board[0][0] == O and board[0][1] == O and board[0][2] == O:
        return O
    elif board[1][0] == O and board[1][1] == O and board[1][2] == O:
        return O
    elif board[2][0] == O and board[2][1] == O and board[2][2] == O:
        return O
    elif board[0][0] == O and board[1][0] == O and board[2][0] == O:
        return O
    elif board[0][1] == O and board[1][1] == O and board[2][1] == O:
        return O
    elif board[0][2] == O and board[1][2] == O and board[2][2] == O:
        return O
    elif board[0][0] == O and board[1][1] == O and board[2][2] == O:
        return O
    elif board[2][0] == O and board[1][1] == O and board[0][2] == O:
        return O

    if board[0][0] == X and board[0][1] == X and board[0][2] == X:
        return X
    elif board[1][0] == X and board[1][1] == X and board[1][2] == X:
        return X
    elif board[2][0] == X and board[2][1] == X and board[2][2] == X:
        return X
    elif board[0][0] == X and board[1][0] == X and board[2][0] == X:
        return X
    elif board[0][1] == X and board[1][1] == X and board[2][1] == X:
        return X
    elif board[0][2] == X and board[1][2] == X and board[2][2] == X:
        return X
    elif board[0][0] == X and board[1][1] == X and board[2][2] == X:
        return X
    elif board[2][0] == X and board[1][1] == X and board[0][2] == X:
        return X

    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is None:
        # all cells have been filled without anyone winning, the function should return True.
        if len(actions(board)) == 0:
            return True
        else:
            return False
    # If the game is over, either because someone has won the game
    if winner(board) == O or winner(board) == X:
        return True
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # If X has won the game, the utility is 1
    if winner(board) == X:
        return 1
    # f O has won the game, the utility is -1
    if winner(board) == O:
        return -1
    # If the game has ended in a tie, the utility is 0.
    # You may assume utility will only be called on a board if terminal(board) is True.
    else:
        return 0


def max_value(state):
    v = -math.inf
    if terminal(state):
        return utility(state)
    for actione in actions(state):
        v = max(v, min_value(result(state, actione)))
    return v


def min_value(state):
    v = +math.inf
    if terminal(state):
        return utility(state)
    for actione in actions(state):
        v = min(v, max_value(result(state, actione)))
    return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    '''
    The minimax function should take a board as input, and return the optimal move for the player to move on that board.

    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. 
    If multiple moves are equally optimal, any of those moves is acceptable.
    If the board is a terminal board, the minimax function should return None.
..........
Given a state s
    The maximizing player picks action a in Actions(s) that produces the highest value of Min-Value(Result(s, a)).
    The minimizing player picks action a in Actions(s) that produces the lowest value of Max-Value(Result(s, a)).
    '''

    if len(actions(board)) >= 8:  # if first move - random move
        from_Set_to_list = list(actions(board))
        returning_one_random_tuple = from_Set_to_list[random.randint(0, len(actions(board)) - 1)]
        return returning_one_random_tuple

    panel = copy.deepcopy(board)  # necessary?probably not

    scores = []
    if player(board) == X:
        for action in actions(board):
            value = min_value(result(panel, action))
            scores.append((value, action))
    else:
        for action in actions(board):
            value = max_value(result(panel, action))
            scores.append((value, action))

    if player(board) == X:
        return max(scores)[1]
    else:
        return min(scores)[1]


'''
    def print_board(board):
        for row in board:
            for value in row:
                if value==None:
                    print("_", " ", end="")
                else:
                    print(value, " ",end="")
            print()
        print()
        '''