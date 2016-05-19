# connectfour.py
#
# ICS 32 Winter 2013
# Project #2: Send Me On My Way

'''
This module is comprised of the game logic that underlies a Connect Four
game, implementing such functionality as tracking the state of a game,
updating that state as players make moves, and determining if there is a
winner.  No user interface or network functionality is included; this is
strictly a collection of tools for implementing the game logic.
'''

import collections


# These constants specify the concepts of "no player", the "red player"
# and the "yellow player".  Your code should use these constants in
# place of their hard-coded values.
NONE = ' '
RED = 'R'
YELLOW = 'Y'


# These constants specify the size of the game board (i.e., the number
# of rows and columns it has).  It should be possible to change these
# constants and re-run your program so that the board will have a
# different size; be sure that you're not hard-coding these values
# anywhere in your own code.
BOARD_COLUMNS = 7
BOARD_ROWS = 6


# ConnectFourGameState is a namedtuple that tracks everything important
# about the state of a Connect Four game as it progresses.  It contains
# two fields:
#
#     'board', which is a two-dimensional list of strings describing
#     the game board.  Each string represents one cell on the board
#     and is either NONE, RED, or YELLOW, depending on whether the
#     cell contains a red piece, a yellow piece, or is empty
#
#     'turn', which specifies which player will make the next move;
#     its value will always be either RED or YELLOW
ConnectFourGameState = collections.namedtuple(
    'ConnectFourGameState', ['board', 'turn'])



# This is the simplest example of how you create new kinds of exceptions
# that are specific to your own program.  We'll see later in the quarter
# in more detail what this notation means; in short, we're introducing
# new types into our program and stating that they have strong similarities
# to the existing type called Exception.


class InvalidConnectFourMoveError(Exception):
    '''Raised whenever an invalid move is made'''
    pass


class ConnectFourGameOverError(Exception):
    '''Raised whenever an attempt is made to make a move after the game is
    already over'''
    pass




# The next four functions are the "public" functions that are provided
# by this module.  You'll need to call all four of these functions, but
# will not need to call any of the others.



def new_game_state():
    '''Returns a ConnectFourGameState representing a brand new game
    in which no moves have been made yet.'''
    return ConnectFourGameState(board=_new_game_board(), turn=RED)



def drop_piece(game_state, column_number):
    '''Given a game state and a column number, returns the game state
    that results when the current player (whose turn it is) drops a piece
    into the given column.  If the column number is invalid, a ValueError
    is raised.  If the game is over, a ConnectFourGameOverError is raised.
    If a move cannot be made in the given column because the column is
    filled already, an InvalidConnectFourMoveError is raised.'''
    _require_valid_column_number(column_number)
    _require_game_not_over(game_state)

    empty_row = _find_bottom_empty_row_in_column(game_state.board, column_number)

    if empty_row == -1:
        raise InvalidConnectFourMoveError()
    else:
        game_state.board[column_number][empty_row] = game_state.turn
        return game_state._replace(turn=_opposite_turn(game_state.turn))



def pop_piece(game_state, column_number):
    '''Given a game state and a column number, returns the game state that
    results when the current player (whose turn it is) pops a piece from the
    bottom of the given column.  If the column number is valid, a ValueError
    is raised.  If the game is over, a ConnectFourGameOverError is raised.
    If a piece cannot be popped from the bottom of the given column because
    the column is empty or because the piece at the bottom of the column
    belongs to the other player, an InvalidConnectFourMoveError is raised.'''
    _require_valid_column_number(column_number)
    _require_game_not_over(game_state)

    if game_state.turn == game_state.board[column_number][BOARD_ROWS - 1]:
        for row in range(BOARD_ROWS - 1, -1, -1):
            game_state.board[column_number][row] = game_state.board[column_number][row - 1]

        game_state.board[column_number][row] = NONE

        return game_state._replace(turn=_opposite_turn(game_state.turn))
    else:
        raise InvalidConnectFourMoveError()



def winning_player(game_state):
    '''Determines the winning player in the given game state, if any.
    If the red player has won, RED is returned; if the yellow player
    has won, YELLOW is returned; if no player has won yet, NONE is
    returned.'''
    winner = NONE
    
    for col in range(BOARD_COLUMNS):
        for row in range(BOARD_ROWS):
            if _winning_sequence_begins_at(game_state.board, col, row):
                if winner == NONE:
                    winner = game_state.board[col][row]
                elif winner != game_state.board[col][row]:
                    # This handles the rare case of popping a piece
                    # causing both players to have four in a row;
                    # in that case, the last player to make a move
                    # is the winner.
                    return _opposite_turn(game_state.turn)

    return winner
    



# Modules often contain functions, variables, or classes whose names begin
# with underscores.  This is no accident; in Python, this is the agreed-upon
# standard for specifying functions, variables, or classes that should be
# treated as "private" or "hidden".  The rest of your program should not
# need to call any of these functions directly; they are utility functions
# called by the functions above, so that those functions can be shorter,
# simpler, and more readable.



def _new_game_board():
    '''Creates a new game board.  Initially, a game board has the size
    BOARD_COLUMNS x BOARD_ROWS and is comprised only of strings with the
    value NONE'''
    board = []

    for col in range(BOARD_COLUMNS):
        board.append([])
        for row in range(BOARD_ROWS):
            board[-1].append(NONE)

    return board



def _find_bottom_empty_row_in_column(board, column_number):
    '''Determines the bottommost empty row within a given column, useful
    when dropping a piece; if the entire column in filled with pieces,
    this function returns -1'''
    for i in range(BOARD_ROWS - 1, -1, -1):
        if board[column_number][i] == NONE:
            return i

    return -1



def _opposite_turn(turn):
    '''Given the player whose turn it is now, returns the opposite player'''
    if turn == RED:
        return YELLOW
    else:
        return RED



def _winning_sequence_begins_at(board, col, row):
    '''Returns True if a winning sequence of pieces appears on the board
    beginning in the given column and row and extending in any of the
    eight possible directions; returns False otherwise'''
    return _four_in_a_row(board, col, row, 0, 1) \
            or _four_in_a_row(board, col, row, 1, 1) \
            or _four_in_a_row(board, col, row, 1, 0) \
            or _four_in_a_row(board, col, row, 1, -1) \
            or _four_in_a_row(board, col, row, 0, -1) \
            or _four_in_a_row(board, col, row, -1, -1) \
            or _four_in_a_row(board, col, row, -1, 0) \
            or _four_in_a_row(board, col, row, -1, 1)
    


def _four_in_a_row(board, col, row, coldelta, rowdelta):
    '''Returns True if a winning sequence of pieces appears on the board
    beginning in the given column and row and extending in a direction
    specified by the coldelta and rowdelta'''
    start_cell = board[col][row]

    if start_cell == NONE:
        return False
    else:
        for i in range(1, 4):
            if not _is_valid_column_number(col + coldelta * i) \
                    or not _is_valid_row_number(row + rowdelta * i) \
                    or board[col + coldelta *i][row + rowdelta * i] != start_cell:
                return False
        return True
    


def _require_valid_column_number(column_number):
    '''Raises a ValueError if its parameter is not a valid column number'''
    if type(column_number) != int or not _is_valid_column_number(column_number):
        raise ValueError('column_number must be int between 0 and {}'.format(BOARD_COLUMNS - 1))



def _require_game_not_over(game_state):
    '''Raises a ConnectFourGameOverError if the given game state represents
    a situation where the game is over (i.e., there is a winning player)'''
    if winning_player(game_state) != NONE:
        raise ConnectFourGameOverError()



def _is_valid_column_number(column_number):
    '''Returns True if the given column number is valid; returns False
    otherwise'''
    return 0 <= column_number < BOARD_COLUMNS



def _is_valid_row_number(row_number):
    '''Returns True if the given row number is valid; returns False
    otherwise'''
    return 0 <= row_number < BOARD_ROWS
