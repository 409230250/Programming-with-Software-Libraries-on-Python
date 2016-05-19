##Junjie Lin 25792830

import state
import start1

def main():
    '''Game function. '''

    connection = start1.GreetingApplication()._on_greet()

    row = int(connection[0])
    column = int(connection[1])
    turn = connection[2]
    top = connection[3]
    win = connection[4]

    board = state.makeNewBoard(row, column)
    state.get_board(board,row, column, top)
    while True:
        if turn == 'black':
            symbol = 'B'
            print_board(board, row)
            scores = state.show_scores(board, row, column)
            print('Black: {}; White: {}'.format(scores[0],scores[1]))
            print("\nIt is {}'s turn, {} is '{}'.".format('Black','Black',symbol))
            move = every_move(board, symbol, row, column)
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
            print_board(board, row)
            scores = state.show_scores(board, row, column)
            print('Black: {}; White: {}'.format(scores[0],scores[1]))
            print("\nIt is {}'s turn, {} is '{}'.".format('White','White',symbol))
            move = every_move(board, symbol, row, column)
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
def connect():
    number = ['4','6','8', '10']
    while True:
        row = input('Please enter even number from 4-10 for your row umber:')
        if not row in number:
           continue
        break
    while True:
        column = input('Please enter even number from 4-10 for your column number:')
        if not column in number:
            continue
        break
    while True:
        move_first = input("Please enter 'b' for black or 'w' for white move first: ")
        turn=''
        if move_first == 'b':
            turn = 'black'
            break
        elif move_first == 'w':
            turn = 'white'
            break
        else:
            continue
    while True:
        top = input("Do you want the top pieces to be 'wb' or 'bw':")
        if top != 'wb' and top != 'bw':
            continue
        break
    while True:
        win = input("Do you want the person has more pieces win or the less win? Enter 'more' or 'less':")
        if win != 'more' and win != 'less':
            continue
        break
    return [row, column, turn, top, win]
####################################################################
## Get Input and Return Correct Move:
def every_move(board, symbol, row, column):
    '''Ask user to put in number and check the number
       if there is a valid place. Otherwise, ask again.'''

    number=['1','2','3','4','5','6','7','8','9','10']
    while True:
        move_column = input("Please enter the column of your move into the grid:")
        move_row = input('Please enter the row of your move into the grid:')
        if len(move_column) > 2 and len(move_row) > 2:
            print("The length of your input has to be 2. Please try again.")
            continue
        try:
            x = int(move_column)
            y = int(move_row)
        except:
            print('The type of the inputs have to be (int).')
            continue

        if not move_column in number or not move_row in number:
            print('Please enter input as number within your column and row. Please try again.')
            continue

        if int(move_column) > column or int(move_row) > row:
            print('Both (XY)in input should should not greater than the column or row. Please try again.')
            continue
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
