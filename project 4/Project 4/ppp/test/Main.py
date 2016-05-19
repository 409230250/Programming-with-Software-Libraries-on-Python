##Junjie Lin 25792830
import Move 
import Check #check if the input is valid or not.

def main(turn, symbol_player, symbol_computer, board):
    '''Game function. '''
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
            move = every_move(board, symbol_player)
            print('Your move is at {}.'.format(tell_move(move)))
            Move.MakeMove(board,symbol_player).make_move_for_board(move[0],move[1])

            if check_score(show_scores(board)) != 36:
                if Move.MakeMove(board,symbol_computer).Flip_pieces() == []:
                    print("!!Computer has no where to move; it's player's turn!!")
                    turn = 'player'
                else:
                    turn = 'computer'
            else:
                break

        else:
            if False:
                validMovesBoard = getBoard_ValidMoves(board, symbol_computer)
                print_board(validMovesBoard)
            else:
                print_board(board)

            scores = show_scores(board)
            print('Player has {} points and computer has {} points.'.format(scores[0],scores[1]))
            print("\nIt is {}'s turn, {} is '{}'.".format(turn,turn,symbol_computer))
            move = every_move(board, symbol_computer)
            print('Your move is at {}.'.format(tell_move(move)))
            Move.MakeMove(board,symbol_computer).make_move_for_board(move[0],move[1])

            if check_score(show_scores(board)) != 36:
                if Move.MakeMove(board,symbol_player).Flip_pieces() == []:
                    print("!!Player has no where to move; it's computer's turn!!")
                    turn = 'computer'
                else:
                    turn = 'player'
            else:
                break

    print_board(board)
    scores = show_scores(board)
    print('Player has {} points and computer has {} points.'.format(scores[0],scores[1]))
    who_won(scores)

####################################################################
## Get Input and Return Correct Move:
def every_move(board, symbol):
    '''Ask user to put in number and check the number
       if there is a valid place. Otherwise, ask again.'''

    number=['1','2','3','4','5','6']
    while True:
        move = input("Please enter your move as 'XY' on the grid:")
        if len(move) != 2:
            print("The length of your input has to be 2. Please try again.")
            continue

        if not move[0] in number and not move[1] in number:
            print('The type of the input has to be (int) and each of them should should from 1-6. Please try again.')
            continue
        try:
            x = int(move[0])-1
            y = int(move[1])-1
            if Check.ValidMoves(board, symbol, x, y).can_move() == False:
                raise Error
        except:
            print("Not a valid move, please try again.")
            continue
        break
    return [x,y]

################################################################
## Scores: 
def check_score(scores):
    '''Uses the scores of both computer and player and returns the total.'''
    return scores[0]+scores[1]            
      
def tell_move(a):
    '''Tell the user where he/she put in.'''
    z=a[0]+1
    w=a[1]+1
    return [z,w]

def show_scores(board):
    '''Count both of the player's scores and computer's scores.
       Then return them.'''
    
    Bscores=0
    Wscores=0
    for i in range(6):
        for a in range(6):
            if board[i][a] == 'B':
                Bscores+=1
            elif board[i][a] == 'W':
                Wscores+=1
    return [Bscores,Wscores]

def who_won(scores):
    '''Check either player won or computer won by the higher scores and print it out.
       It also can be a draw game.'''
    if scores[0] > scores[1]:
        print('Player won the game!')
    elif scores[0] < scores[1]:
        print('Computer won the game!')
    else:
        print('This game is draw.')

#####################################################################
## Getting Copy:
def getBoardCopy(board):
    ''' Makes a copy of the new empty board and returns to
        function, getBoard_ValidMoves.'''
    copy_of_new_board = makeNewBoard()
    for x in range(6):
        for y in range(6):
            copy_of_new_board[x][y] = board[x][y]
    return copy_of_new_board

def getBoard_ValidMoves(board, symbol):
    ''' Updates the new board by using the function Flip_pieces
        and returns the update board.'''
    copy_of_get_board = getBoardCopy(board)
    for x, y in Flip_pieces(board, symbol):
        copy_of_get_board[x][y] = '.'
    return copy_of_get_board

#################################################################
## Board:
def makeNewBoard():
    '''Make a new empty board. It is a list that has six lists of
       six empty strings. Then return it.'''
    board = []
    for i in range(6):
        board.append([])
        for j in range(6):
            board[i].append(' ')  
    return board

def get_board(board):
    '''Let the board have four pazzles in the beginning.'''
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
    
################################################################

if __name__ == '__main__':
    board = makeNewBoard()
    get_board(board)
    turn = 'player'
    symbol_player, symbol_computer = 'B', 'W'
    print('Game start!\n')
    main(turn, symbol_player, symbol_computer, board)
