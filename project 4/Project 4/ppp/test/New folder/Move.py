import Check

class MakeMove:
    def __init__(self, board, symbol):
        self.board = board
        self.symbol = symbol

    def make_move_for_board(self, x, y):
        '''Use the correct input and update it into the board.'''
        
        TrueorFalse = Check.ValidMoves(self.board, self.symbol, x, y).can_move()
        if TrueorFalse == False:
            return False
        else:
            self.board[x][y] = self.symbol
            for x,y in TrueorFalse:
                self.board[x][y] = self.symbol
        return True

    def Flip_pieces(self):
        '''Check all of the pazzles if they can be flipped by the input
           and return a updated board to function getBoard_ValidMoves.'''
        
        result = []
        for h in range(6):
            for v in range(6):
                if Check.ValidMoves(self.board, self.symbol, h, v).can_move() != False:
                    result.append([h, v])
        return result
