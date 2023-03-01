"""
Tic Tac Toe Player
"""

import math
from copy import deepcopy

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
    # for i in range(3):
    #     for j in range(3):
    #         if not board[i][j]:
    #             return X
       
    x_count = 0
    o_count = 0
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
            
    if x_count > o_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions = set()
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                possible_actions.add((i, j))
                
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_temp = deepcopy(board)
    
    if not board_temp[action[0]][action[1]]:
        board_temp[action[0]][action[1]] = player(board)
    else:
        raise Exception("Invalid Move")
    
    return board_temp
        
            


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Horizontal Check
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == X:
                return X
        if board[i][0] == board[i][1] == board[i][2] == O:
                return O


    # Vertical Check
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] == X:
                return X
            
        if board[0][i] == board[1][i] == board[2][i] == O:
                return O
            
            
    # Diagonal Check
    if board[0][0] == board[1][1] == board[2][2] == X or board[2][0] == board[1][1] == board[0][2] == X:
        return X

    if board[0][0] == board[1][1] == board[2][2] == O or board[2][0] == board[1][1] == board[0][2] == O:
        return O

    return None
            


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) == X:
        return True
    elif winner(board) == O:
        return True
    
    for i in range(3):
        for j in range(3):
            if not board[i][j]:
                return False
    
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board):
        return None
    
    availablePlays = []
    
    if player(board) == X:
        for action in actions(board):
            availablePlays.append((action ,min_value(result(board, action))))
        return sorted(availablePlays, key=lambda v: v[1], reverse=True)[0][0]

    else:
        for action in actions(board):
            availablePlays.append((action, max_value(result(board, action))))
        return sorted(availablePlays, key=lambda v: v[1])[0][0]
       
       
def max_value(board):
    if terminal(board):
        return utility(board)
    
    v = float("-inf")
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v

def min_value(board):
    if terminal(board):
        return utility(board)
    
    v = float("inf")
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v