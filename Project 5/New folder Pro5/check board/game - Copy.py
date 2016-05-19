##Junjie Lin 25792830

import state
import inputs
import BoardCopy
def main():
    '''Game function. '''
    while True:
        connection = inputs.check_input()
        if connection == False:
            continue
        else:
            break

    print('\nColumn: {}'.format(connection[0]),
          '\nRow: {}'.format(connection[1]),
          '\nFirst Turn: {}'.format(connection[2]),
          '\nWB Setting: {}'.format(connection[3]),
          '\nWin by: {}\n'.format(connection[4]))

    column = connection[0]
    row = connection[1]
    turn = connection[2]
    top = connection[3]
    win = connection[4]
    
    board = state.makeNewBoard(row, column)
    state.get_board(board, row, column, top)

    while True:
        if turn == 'black':
            symbol = 'B'
##            print_board(board, row)
##            print(BoardCopy.BoardApplication(column,row, top)._on_mouse_click())
            
##            scores = state.show_scores(board, row, column)
##            print('Black: {}; White: {}'.format(scores[0],scores[1]))
            print("\nIt is {}'s turn, {} is '{}'.".format('Black','Black',symbol))
            move = every_move(board, symbol, row, column, top)
            print('Your move is at {}.'.format(state.tell_move(move)))
            state.MakeMove(board,symbol, row, column).make_move_for_board(move[0],move[1])
            if state.check_score(state.show_scores(board, row, column)) != (row*column):
                if state.MakeMove(board, 'W', row, column).Flip_pieces() == []:
                    print("!!White has no where to move; it's black turn!!")
                    turn = 'black'
                else:
                    turn = 'white'
            else:
                break
        else:
            symbol = 'W'
##            print_board(board, row)
##            scores = state.show_scores(board, row, column)
##            print('Black: {}; White: {}'.format(scores[0],scores[1]))
            print("\nIt is {}'s turn, {} is '{}'.".format('White','White',symbol))
            move = every_move(board, symbol, row, column, top)
            print('Your move is at {}.'.format(state.tell_move(move)))
            state.MakeMove(board,symbol, row, column).make_move_for_board(move[0],move[1])
            if state.check_score(state.show_scores(board, row, column)) != (row*column):
                if state.MakeMove(board,'B', row, column).Flip_pieces() == []:
                    print("!!Black has no where to move; it's white turn!!")
                    turn = 'white'
                else:
                    turn = 'black'
            else:
                break

    print_board(board, row)
    scores = state.show_scores(board, row, column)
    print('Black: {}; White: {}'.format(scores[0],scores[1]))
    who_won(scores, win)
####################################################################
def connect(column, row, move_first, top, win):
    if not row in number:
        print('Not a valid row.')
        return False
    if not column in number:
        print('Not a valid column.')
        return False
    turn=''
    if move_first == 'b':
        turn = 'black'
    elif move_first == 'w':
        turn = 'white'
    else:
        print('Not a valid first move imput.')
        return False
    if top != 'wb' and top != 'bw':
        print('Not a valid input, wb or bw.')
        return False
    if win != 'more' and win != 'less':
        print('Not a valid input of how to win.')
        return False
####################################################################
## Get Input and Return Correct Move:
def every_move(board, symbol, row, column, top):
    '''Ask user to put in number and check the number
       if there is a valid place. Otherwise, ask again.'''

##    number=['1','2','3','4','5','6','7','8','9','10']
    while True:
##        move_column = input("Please enter the column of your move into the grid:")
##        move_row = input('Please enter the row of your move into the grid:')
##        if len(move_column) > 2 and len(move_row) > 2:
##            print("The length of your input has to be 2. Please try again.")
##            continue
##        try:
##            x = int(move_column)
##            y = int(move_row)
##        except:
##            print('The type of the inputs have to be (int).')
##            continue
##
##        if not move_column in number or not move_row in number:
##            print('Please enter input as number within your column and row. Please try again.')
##            continue
##  
##        if int(move_column) > column or int(move_row) > row:
##            print('Both (XY)in input should should not greater than the column or row. Please try again.')
##            continue
        get_x_y = BoardCopy.BoardApplication(column,row, top)._pass_xandy()
        x= get_x_y[0]
        y= get_x_y[1]
        try:
            x = x-1
            y = y-1
            if state.can_move(board, symbol, x, y, row, column) == False:
                raise Error
        except:
            print("Not a valid move, please try again.")
            continue
        break
    return [x,y]

def print_board(board, row):
    '''Print out board.'''
    number=''
    for i in range(len(board)):
        number+=str(i+1)+'  '
    print('   {:2}'.format(number))
    for num in range(row):
        result=''
        for lst in board:
            if lst[num] == ' ':
                result+='.  '
            else:
                result+=lst[num]+'  '
        print('{:2} {:2}'.format(num+1,result))

def who_won(scores, win):
    '''Check either player won or computer won by the higher scores and print it out.
       It also can be a draw game.'''
    if win == 'more':
        if scores[0] > scores[1]:
            print('Black won the game!')
        elif scores[0] < scores[1]:
            print('White won the game!')
        else:
            print('This game is draw.')
    else:
        if scores[0] < scores[1]:
            print('Black won the game!')
        elif scores[0] > scores[1]:
            print('White won the game!')
        else:
            print('This game is draw.')
        
################################################################
if __name__ == '__main__':
    print('Game start!')
    main()
