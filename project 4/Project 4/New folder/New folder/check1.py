##
def can_move(board, symbol, oldx, oldy):
    if board[oldx][oldy] != ' ' and within_board(oldx, oldy):
        return False
        
    board[oldx][oldy] = symbol 
    Flip = []
    for XH, YV in neighbor():
        x, y = oldx, oldy
        x += XH 
        y += YV 
        if within_board(x, y) and board[x][y] == sign(symbol):
            x += XH
            y += YV
            
            if not within_board(x, y):
                continue
            while board[x][y] == sign(symbol):
                x += XH
                y += YV
                if not within_board(x, y):
                    break
                
            if not within_board(x, y):
                continue
            if board[x][y] == symbol:
                while True:
                    x -= XH
                    y -= YV
                    if x == oldx and y == oldy:
                        break
                    Flip.append([x, y])

    board[oldx][oldy] = ' ' 
    if len(Flip) == 0: 
        return False
    return Flip

def within_board(x, y):
    return x >= 0 and x <= 6 and y >= 0 and y <=6

def neighbor():
    return [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

def sign(symbol):
    if symbol == 'B':
        othersymbol = 'W'
    else:
        othersymbol = 'B'
    return othersymbol




























