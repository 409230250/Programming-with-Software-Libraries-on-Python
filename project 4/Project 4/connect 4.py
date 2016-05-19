import collections

NONE = ' '
RED = 'R'
YELLOW = 'Y'

BOARD_COLUMNS = 7
BOARD_ROWS = 6

ConnectFourGameState = collections.namedtuple(
    'ConnectFourGameState', ['board', 'turn'])

class InvalidConnectFourMoveError(Exception):
    pass

class ConnectFourGameOverError(Exception):
    pass

def new_game_state():
    return ConnectFourGameState(board=_new_game_board(), turn=RED)

def drop_piece(game_state, column_number):
    if type(column_number) != int or not _is_valid_column_number(column_number):
        raise ValueError('column_number must be int between 0 and {}'.format(BOARD_COLUMNS - 1))
##    
    if winning_player(game_state) != NONE:
        raise ConnectFourGameOverError()
##
    empty_row = _find_bottom_empty_row_in_column(game_state.board, column_number)

    if empty_row == -1:
        raise InvalidConnectFourMoveError()
    else:
        game_state.board[column_number][empty_row] = game_state.turn
        return game_state._replace(turn=_opposite_turn(game_state.turn))

def pop_piece(game_state, column_number):
    if type(column_number) != int or not _is_valid_column_number(column_number):
        raise ValueError('column_number must be int between 0 and {}'.format(BOARD_COLUMNS - 1))
##    
    if winning_player(game_state) != NONE:
        raise ConnectFourGameOverError()

    if game_state.turn == game_state.board[column_number][BOARD_ROWS - 1]:
        for row in range(BOARD_ROWS - 1, -1, -1):
            game_state.board[column_number][row] = game_state.board[column_number][row - 1]

        game_state.board[column_number][row] = NONE

        return game_state._replace(turn=_opposite_turn(game_state.turn))
    else:
        raise InvalidConnectFourMoveError()

def winning_player(game_state):
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
    
def _new_game_board():
    board = []
    for col in range(BOARD_COLUMNS):
        board.append([])
        for row in range(BOARD_ROWS):
            board[-1].append(NONE)

    return board

def _find_bottom_empty_row_in_column(board, column_number):
    for i in range(BOARD_ROWS - 1, -1, -1):
        if board[column_number][i] == NONE:
            return i

    return -1

def _opposite_turn(turn):
    if turn == RED:
        return YELLOW
    else:
        return RED

def _winning_sequence_begins_at(board, col, row):
    return _four_in_a_row(board, col, row, 0, 1) \
            or _four_in_a_row(board, col, row, 1, 1) \
            or _four_in_a_row(board, col, row, 1, 0) \
            or _four_in_a_row(board, col, row, 1, -1) \
            or _four_in_a_row(board, col, row, 0, -1) \
            or _four_in_a_row(board, col, row, -1, -1) \
            or _four_in_a_row(board, col, row, -1, 0) \
            or _four_in_a_row(board, col, row, -1, 1)
    

def _four_in_a_row(board, col, row, coldelta, rowdelta):
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
    if type(column_number) != int or not _is_valid_column_number(column_number):
        raise ValueError('column_number must be int between 0 and {}'.format(BOARD_COLUMNS - 1))

def _require_game_not_over(game_state):
    if winning_player(game_state) != NONE:
        raise ConnectFourGameOverError()

def _is_valid_column_number(column_number):
    return 0 <= column_number < BOARD_COLUMNS

def _is_valid_row_number(row_number):
    return 0 <= row_number < BOARD_ROWS
