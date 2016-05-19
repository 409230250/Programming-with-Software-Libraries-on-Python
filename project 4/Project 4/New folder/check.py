##
def within_board(x, y):
    # Returns True if the coordinates are located on the board.
    return x >= 0 and x <= 7 and y >= 0 and y <=7

def can_move(board, symbol, oldx, oldy):
    # Returns False if the player's move on space oldx, oldy is invalid.
    # If it is a valid move, returns a list of spaces that would become the player's if they made a move here.
    if board[oldx][oldy] != ' ' and within_board(oldx, oldy):
        return False
        
    board[oldx][oldy] = symbol # temporarily set the symbol on the board.

    if symbol == 'X':
        othersymbol = 'O'
    else:
        othersymbol = 'X'

    Flip = []
    for XH, YV in [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]:
        x, y = oldx, oldy
        x += XH # first step in the direction
        y += YV # first step in the direction
        if within_board(x, y) and board[x][y] == othersymbol:
            # There is a piece belonging to the other player next to our piece.
            x += XH
            y += YV
            if not within_board(x, y):
                continue
            while board[x][y] == othersymbol:
                x += XH
                y += YV
                if not within_board(x, y): # break out of while loop, then continue in for loop
                    break
            if not within_board(x, y):
                continue
            if board[x][y] == symbol:
                # There are pieces to flip over. Go in the reverse direction until we reach the original space, noting all the symbols along the way.
                while True:
                    x -= XH
                    y -= YV
                    if x == oldx and y == oldy:
                        break
                    Flip.append([x, y])

    board[oldx][oldy] = ' ' # restore the empty space
    if len(Flip) == 0: # If no symbols were flipped, this is not a valid move.
        return False
    return Flip

