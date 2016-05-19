##Junjie Lin 25792830

import state

def main(board, turn, row, column, ):
    while True:
        if turn == 'black':
            symbol = 'B'
            print(board)
##            scores = state.show_scores(board, row, column)
##            print('Black: {}; White: {}'.format(scores[0],scores[1]))
##            print("\nIt is {}'s turn, {} is '{}'.".format('Black','Black',symbol))
##            move = every_move(board, symbol, row, column)
##            print('Your move is at {}.'.format(state.tell_move(move)))
##            state.MakeMove(board,symbol, row, column).make_move_for_board(move[0],move[1])
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
            print(board)
##            scores = state.show_scores(board, row, column)
##            print('Black: {}; White: {}'.format(scores[0],scores[1]))
##            print("\nIt is {}'s turn, {} is '{}'.".format('White','White',symbol))
##            move = every_move(board, symbol, row, column)
##            print('Your move is at {}.'.format(state.tell_move(move)))
##            state.MakeMove(board,symbol, row, column).make_move_for_board(move[0],move[1])
            if state.check_score(state.show_scores(board, row, column)) != (row*column):
                if state.MakeMove(board,'B', row, column).Flip_pieces() == []:
                    print("!!Black has no where to move; it's white turn!!")
                    turn = 'white'
                else:
                    turn = 'black'
            else:
                break

    print(board)
    scores = state.show_scores(board, row, column)
    who_won(scores, win)


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

