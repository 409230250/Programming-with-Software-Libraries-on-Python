##Junjie Lin 25792830


##
def change_turn(turn):
    if turn == 'W':
        turn = 'B'
    else:
        turn = 'W'
    return turn 
    
    

## Scores:
def check_score(scores):
    '''Uses the scores of both computer and player and returns the total.'''
    return scores[0]+scores[1]            
      
def tell_move(a):
    '''Tell the user where he/she put in.'''
    z=a[0]+1
    w=a[1]+1
    return [z,w]

def show_scores(board, row, column):
    '''Count both of the player's scores and computer's scores.
       Then return them.'''
    
    Bscores=0
    Wscores=0
    for i in range(column):
        for a in range(row):
            if board[i][a] == 'B':
                Bscores+=1
            elif board[i][a] == 'W':
                Wscores+=1
    return [Bscores,Wscores]

#################################################################
## Board:
def makeNewBoard(row, column):
    '''Make a new empty board. It is a list that has six lists of
       six empty strings. Then return it.'''
    board = []
    for i in range(column):
        board.append([])
        for j in range(row):
            board[i].append(' ')  
    return board

def get_board(board, row, column, top):
    '''Let the board have four pazzles in the beginning.'''
    for i in range(column):
        for j in range(row):
            board[i][j]=(' ')  
    c = int(column/2)
    r = int(row/2)
    top=top.upper()
    board[c][r],board[c-1][r-1],board[c-1][r],board[c][r-1] = top[0],top[0],top[1],top[1]

##################################################################################
class MakeMove:
    def __init__(self, board, symbol, row, column):
        self.board = board
        self.symbol = symbol
        self.row = row
        self.column = column
        
    def make_move_for_board(self, x, y):
        TrueorFalse = can_move(self.board, self.symbol, x, y, self.row, self.column)
        if TrueorFalse == False:
            return False
        else:
            self.board[x][y] = self.symbol
            for x,y in TrueorFalse:
                self.board[x][y] = self.symbol
        return True

    def Flip_pieces(self):
        result = []
        for h in range(self.column):
            for v in range(self.row):
                if can_move(self.board, self.symbol, h, v, self.row, self.column) != False:
                    result.append([h, v])
        return result

############################################################################
def can_move(board, symbol, oldx, oldy, row, column):
    '''Check either it's a valid move or not.
       If so, return Flip(flip pieces with oppsive color)'''
    
    if board[oldx][oldy] != ' ' and within_board(oldx, oldy, row, column):
        return False  
    board[oldx][oldy] = symbol 
    Flip = []
    for XH, YV in neighbor():
        x, y = oldx, oldy
        x += XH 
        y += YV 
        if within_board(x, y, row, column) and board[x][y] == sign(symbol):
            x += XH
            y += YV
            
            if not within_board(x, y, row, column):
                continue
            while board[x][y] == sign(symbol):
                x += XH
                y += YV
                if not within_board(x, y, row, column):
                    break
                
            if not within_board(x, y, row, column):
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

def within_board(x, y, row, column):
    '''return the range of row and column'''
    return x >= 0 and x <= (column-1) and y >= 0 and y <=(row-1)

def neighbor():
    '''return different direction of [x,y]'''
    return [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]

def sign(symbol):
    '''change the symbol of black to white and white to black.'''
    if symbol == 'B':
        othersymbol = 'W'
    else:
        othersymbol = 'B'
    return othersymbol
