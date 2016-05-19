
class ValidMoves:
    def __init__(self, board, symbol, oldx, oldy):
        self.board = board
        self.symbol = symbol
        self.oldx = oldx
        self.oldy = oldy

    def can_move(self):
        if self.board[self.oldx][self.oldy] != ' ' and ValidMoves.within_board(self.oldx, self.oldy):
            return False
        self.board[self.oldx][self.oldy] = self.symbol 

        if self.symbol == 'B':
            othersymbol = 'W'
        else:
            othersymbol = 'B'

        Flip = []
        for XH, YV in ValidMoves.neighbor():
            x, y = self.oldx, self.oldy
            x += XH 
            y += YV
            if ValidMoves.within_board(x, y) and self.board[x][y] == othersymbol:
                x += XH
                y += YV
                if not ValidMoves.within_board(x, y):
                    continue
                while self.board[x][y] == othersymbol:
                    x += XH
                    y += YV
                    if not ValidMoves.within_board(x, y):
                        break
                    
                if not ValidMoves.within_board(x, y):
                    continue
                if self.board[x][y] == self.symbol:
                    while True:
                        x -= XH
                        y -= YV
                        if x == self.oldx and y == self.oldy:
                            break
                        Flip.append([x, y])

        self.board[self.oldx][self.oldy] = ' ' 
        if len(Flip) == 0:
            return False
        return Flip

    def within_board(x, y):
        return x >= 0 and x <= 6 and y >= 0 and y <=6

    def neighbor():
        return [[0, 1], [1, 1], [1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1]]


