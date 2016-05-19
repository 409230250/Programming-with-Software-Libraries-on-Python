##Junjie Lin 25792830
import check
def get_board():
    board = []
    for i in range(8):
        board.append([])
        for j in range(8):
            board[i].append(' ')  
    board[3][3], board[4][4], board[3][4], board[4][3] = 'X','X','O','O'
    return board

def make_move_for_board(board,symbol,x,y):
    TrueorFalse = check.can_move(board,symbol,x,y)
    if TrueorFalse == False:
        return False
    else:
        board[x][y] = symbol
        for x,y in TrueorFalse:
            board[x][y] = symbol
    return True
        
def print_board(board:list):
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
        
##########################################
def every_move(symbol):
    number=['1','2','3','4','5','6','7','8']
    while True:
        move = input("Please enter your move as 'XY' in the grid:")
        if len(move) == 2 and move[0] in number and move[1] in number:
            x = int(move[0])-1
            y = int(move[1])-1
            if check.can_move(board, symbol, x, y) == False:
                continue
##check if it is not a valid move, ask user to enter again.
            else:
                break
##check if it is a valid move, use the input as x,y to update board.
        else:
            print("Not a valid move, please try again.")
            every_move(symbol)
    return [x,y]

def tell_move(a):
    z=a[0]+1
    w=a[1]+1
    return [z,w]
    

def Flip_pieces(board, symbol):
    validMoves = []
    for x in range(8):
        for y in range(8):
            if check.can_move(board, symbol, x, y) != False:
                validMoves.append([x, y])
    return validMoves


if __name__ == '__main__':
    board = get_board()
    turn = 'player'
    symbol_player, symbol_computer = 'X', 'O'
    print('Game start!\n')
    while True:
        if turn == 'player':
            print_board(board)
            print("\nIt is {}'s turn, {} is '{}'.".format(turn,turn,symbol_player))
            
            move = every_move(symbol_player)
            show_move = tell_move(move)
            print('Your move is at {}.\n'.format(show_move))
            make_move_for_board(board,symbol_player,move[0],move[1])

            if Flip_pieces(board,symbol_computer) == []:
                break
            else:
                turn = 'computer'

        else:
            print_board(board)
            print("\nIt is {}'s turn, {} is '{}'.".format(turn,turn,symbol_computer))
            move = every_move(symbol_computer)
            show_move = tell_move(move)
            print('Your move is at {}.\n'.format(show_move))
            make_move_for_board(board,symbol_computer,move[0],move[1])
            if Flip_pieces(board,symbol_player) == []:
                break
            else:
                turn = 'player'
    else:
        print('Done!')

