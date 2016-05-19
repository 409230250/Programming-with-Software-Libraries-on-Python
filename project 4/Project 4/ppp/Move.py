import VM

class MakeMove:
    def __init__(self, board, symbol):
        self.board = board
        self.symbol = symbol

    def every_move(self):
        '''Ask user to put in number and check the number
           if there is a valid place. Otherwise, ask again.'''

        number=['1','2','3','4','5','6','7','8']
        while True:
            move = input("Please enter your move as 'XY' on the grid:")
            if not len(move) == 2:
                print("The length of your input has to be 2. Please try again.")
                continue
            if not move[0] in number and not move[1] in number:
                print('The type of the input has to be int and there are 1-8. Please try again.')
                continue
            try:
                x = int(move[0])-1
                y = int(move[1])-1
                if VM.ValidMoves(self.board, self.symbol, x, y).can_move() == False:
                    raise Error
            except:
                print("Not a valid move, please try again.")
                continue
            break
        return [x,y]

    def make_move_for_board(self, x, y):
        '''Use the correct input and update that one into the board.
        '''
        TrueorFalse = VM.ValidMoves(self.board, self.symbol, x, y).can_move()
        if TrueorFalse == False:
            return False
        else:
            self.board[x][y] = self.symbol
            for x,y in TrueorFalse:
                self.board[x][y] = self.symbol
        return True

    def Flip_pieces(self, x, y):
        '''Check all of the pazzles if they need to be flip by the input
           and update them into the board. Then return a updated board.'''
        
        result = []
        for x in range(8):
            for y in range(8):
                if VM.ValidMoves(self.board, self.symbol, x, y).can_move() != False:
                    result.append([x, y])
        return result
