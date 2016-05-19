##Junjie Lin 25792830
import VM
import Move

def main(turn, symbol_player, symbol_computer, board):
    while True:
        if turn == 'player':
            if False:
                validMovesBoard = getBoard_ValidMoves(board, symbol_player)
                print_board(validMovesBoard)
            else:
                print_board(board)

            show_scores(board)
            print("\nIt is {}'s turn, {} is '{}'.".format(turn,turn,symbol_player))
            move = Move.MakeMove(board, symbol_player).every_move()
            print('Your move is at {}.'.format(tell_move(move)))
            Move.MakeMove(board,symbol_player).make_move_for_board(move[0],move[1])

            if Move.MakeMove(board,symbol_computer).Flip_pieces(move[0],move[1]) == []:
                turn = change_turn(turn)
            else:
                turn = change_turn(turn)

        else:
            if False:
                validMovesBoard = getBoard_ValidMoves(board, symbol_computer)
                print_board(validMovesBoard)
            else:
                print_board(board)

            show_scores(board)
            print("\nIt is {}'s turn, {} is '{}'.".format(turn,turn,symbol_computer))
            move = Move.MakeMove(board, symbol_computer).every_move()
            print('Your move is at {}.'.format(tell_move(move)))
            Move.MakeMove(board,symbol_computer).make_move_for_board(move[0],move[1])
            if Move.MakeMove(board,symbol_computer).Flip_pieces(move[0],move[1]) == []:
                turn = change_turn(turn)
            else:
                turn = change_turn(turn)
    print_board(board)
    scores = show_scores(board)
    who_won(scores)

########################################################################
def change_turn(turn):
    if turn == 'player':
        return 'computer'
    else:
        return 'player'


def print_board(board:list):
    '''Print out board.'''
    number=''
    for i in range(len(board)):
        number+=str(i+1)+'  '
    print('  {}'.format(number))
    for num in range(len(board)):
        result=''
        for lst in board:
            if lst[num] == ' ':
                result+='.  '
            else:
                result+=lst[num]+'  '
        print('{} {}'.format(num+1,result))
        
def tell_move(a):
    '''Tell the user where did he/she put in as '[X,Y]'.
    '''
    z=a[0]+1
    w=a[1]+1
    return [z,w]

def show_scores(board):
    '''Count both of the player's scores and computer's scores.
       Then return them.'''
    
    Bscores=0
    Wscores=0
    for i in range(len(board)-1):
        for a in range(len(board)-1):
            if board[i][a] == 'B':
                Bscores+=1
            elif board[i][a] == 'W':
                Wscores+=1
    print('Player has {} points and computer has {} points.'.format(Bscores,Wscores))
    return [Bscores,Wscores]

def getBoardCopy(board):
    ''' Make a copy of the new empty board and return it.
    '''
    copy_of_new_board = makeNewBoard()

    for x in range(8):
        for y in range(8):
            copy_of_new_board[x][y] = board[x][y]

    return copy_of_new_board

def getBoard_ValidMoves(board, symbol):
    ''' returns a new board and marke the valid moves so that
        player can make.'''
    copy_of_get_board = getBoardCopy(board)
    for x, y in Flip_pieces(board, symbol):
        copy_of_get_board[x][y] = '.'
    return copy_of_get_board

def who_won(scores):
    '''Check either player won or computer won and print it out.'''
    if scores[0] > scores[1]:
        print('Player won the game!')
    elif scores[0] < scores[1]:
        print('Computer won the game!')
    else:
        print('This game is draw.')
#################################################################

def makeNewBoard():
    '''Make a board. It is a list that has eight lists of
       eight empty strings. Then return board'''
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(' ')  
    return board

def get_board(board):
    '''Let the board have four pazzles as a setup.'''
    for i in range(8):
        for j in range(8):
            board[i][j]=(' ')  
    board[3][3], board[4][4], board[3][4], board[4][3] = 'B','B','W','W'

if __name__ == '__main__':
    board = makeNewBoard()
    get_board(board)
    turn = 'player'
    symbol_player, symbol_computer = 'B', 'W'
    print('Game start!\n')
    main(turn, symbol_player, symbol_computer, board)
