##Junjie Lin 25792830
import check1

def makeNewBoard():
    '''Make a board. It is a list that has eight lists of
       eight empty strings. Then return board'''
    board = []
    for i in range(6):
        board.append([])
        for j in range(6):
            board[i].append(' ')  
    return board

def get_board(board):
    '''Let the board have four pazzles as a setup.'''
    for i in range(6):
        for j in range(6):
            board[i][j]=(' ')  
    board[2][2], board[3][3], board[2][3], board[3][2] = 'B','B','W','W'
      
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
        
def every_move(symbol):
    '''Ask user to put in number and check the number
       if there is a valid place. Otherwise, ask again.'''
    
    number=['1','2','3','4','5','6']
    while True:
        move = input("Please enter your move as 'XY' on the grid:")
        if len(move) == 2 and move[0] in number and move[1] in number:
            x = int(move[0])-1
            y = int(move[1])-1
            if check1.can_move(board, symbol, x, y) == False:
                print("Not a valid move, please try again.")
                
                continue
                ##check if it is not a valid move, ask user to enter again.
            else:
                break
                ##check if it is a valid move, use the input as x,y to update board.
        else:
            print("Not a valid move, please try again.")
            every_move(symbol)
    return [x,y]

def make_move_for_board(board,symbol,x,y):
    '''Use the correct input and update that one into the board.
    '''
    TrueorFalse = check1.can_move(board,symbol,x,y)
    if TrueorFalse == False:
        return False
    else:
        board[x][y] = symbol
        for x,y in TrueorFalse:
            board[x][y] = symbol
    return True

def Flip_pieces(board, symbol):
    '''Check all of the pazzles if they need to be flip by the input
       and update them into the board. Then return a updated board.'''
    
    result = []
    for x in range(6):
        for y in range(6):
            if check1.can_move(board, symbol, x, y) != False:
                result.append([x, y])
    return result

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
    return [Bscores,Wscores]


def getBoardCopy(board):
    ''' Make a copy of the new empty board and return it.
    '''
    copy_of_new_board = makeNewBoard()

    for x in range(6):
        for y in range(6):
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

if __name__ == '__main__':
    board = makeNewBoard()
    get_board(board)
    turn = 'player'
    symbol_player, symbol_computer = 'B', 'W'
    print('Game start!\n')
    while True:
        if turn == 'player':
            if False:
                validMovesBoard = getBoard_ValidMoves(board, symbol_player)
                print_board(validMovesBoard)
            else:
                print_board(board)
            scores = show_scores(board)
            print('Player has {} points and computer has {} points.'.format(scores[0],scores[1]))
            print("\nIt is {}'s turn, {} is '{}'.".format(turn,turn,symbol_player))
            
            move = every_move(symbol_player)
            show_move = tell_move(move)
            print('Your move is at {}.'.format(show_move))
            make_move_for_board(board,symbol_player,move[0],move[1])

            if Flip_pieces(board,symbol_computer) == []:
                break
            else:
                turn = 'computer'

        else:
            if False:
                validMovesBoard = getBoard_ValidMoves(board, symbol_player)
                print_board(validMovesBoard)
            else:
                print_board(board)
            scores = show_scores(board)
            print('Player has {} points and computer has {} points.'.format(scores[0],scores[1]))
            print("\nIt is {}'s turn, {} is '{}'.".format(turn,turn,symbol_computer))
            move = every_move(symbol_computer)
            show_move = tell_move(move)
            print('Your move is at {}.'.format(show_move))
            make_move_for_board(board,symbol_computer,move[0],move[1])
            if Flip_pieces(board,symbol_player) == []:
                break
            else:
                turn = 'player'
    print_board(board)
    print('Player has {} points and computer has {} points.'.format(scores[0],scores[1]))
    scores = show_scores(board)
    who_won(scores)

