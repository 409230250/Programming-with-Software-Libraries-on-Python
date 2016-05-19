

#Peter Thai (66218086) and Junjie Lin (25792830) 
import connectfour
import I32CFP



def who_r_you():
    state = connectfour.new_game_state()
    mode=input('Please enter what mode you want to play (s: server, c: client, con: console): ')
    if mode == 's':
        return server(state)
    elif mode == 'c':
        return client(state)
    elif mode == 'con':

        return console()
    
    else:
        print('Error, please try again.')
        who_r_you()

def console():
    state = connectfour.new_game_state()
    winner = ' '
    print_board(state.board)
    while winner == ' ':
        drop_or_pop = input('It\'s ' + state.turn +' turn. Do you want to drop or pop? ')
        while drop_or_pop == 'drop':
            column = input('Which column (0-6) do you want to drop? ')
            newstate = _drop_piece(state,column)
            if state != newstate:
                state = newstate
                winner = connectfour.winning_player(state)
                break

        while drop_or_pop == 'pop':
            try:
                column = input('Which column (0-6) do you want to pop? ')
                newstate = _pop_piece(state,column)
                if state != newstate:
                    state = newstate
                    winner = connectfour.winning_player(state)
                    break
                if state.board == connectfour.new_game_state().board:
                    break
            except:
                print('Error. There is no piece you can pop out.\n'
                      + 'Please look for another column to pop out or you can drop another piece.')
                break
            
        while drop_or_pop != 'drop' and drop_or_pop != 'pop':
            print('Misspell. Please try again, drop or pop?')
            break
    else:
        if winner == 'R':
            print('Red won.')
        elif winner == 'Y':
            print ('Yellow won.')

def _drop_piece(state,column):
    try: 
        column = int(column)
        state = connectfour.drop_piece(state, column)
        print_board(state.board)
    except:
        print("Error.")
    finally:
        return state
        
def _pop_piece(state,column):
    column = int(column)
    state = connectfour.pop_piece(state, column)
    print_board(state.board)
    return state

def print_board(board:list):
    number=''
    for i in range(len(board)):
        number+=str(i)+'  '
    print(number)
    
    for num in range(len(board)-1):
        result=''
        for lst in board:
            if lst[num] == ' ':
                result+='.  '
            else:
                result+=lst[num]+'  '
        print(result)


##server
def server(state):
    stream_socket, from_address = I32CFP.server_side()

    print_board(state.board)
    print('Y is your sign.')
    print('Waiting player to move.')

    winner = ' '
    while winner == ' ':
        winner = makingmove(stream_socket, state, winner)
    if winner == 'R':
        print('Red won.')
    elif winner == 'Y':
        print('Yellow won.')
    I32CFP.close_socket(stream_socket)

        
def makingmove(stream_socket,state, winner):
        line_in = I32CFP.read_move(stream_socket)

        player_game_state = convert_gamestate(state,line_in)
        winner = connectfour.winning_player(state)
        if winner != ' ':
            return winner
        else:
            s_move_ops(player_game_state, stream_socket)
            return winner

def convert_gamestate(state,line_in):
    line_in = line_in.split(' ')
    if line_in[0] == 'DROP':
        return _drop_piece(state,line_in[1])
    elif line_in[0] == 'POP':
        return _pop_piece(state,line_in[1])
    
def s_move_ops(state,socket):
    print('Player {}\'s turn'.format(state.turn))
    move = input('Do you want to drop or pop? ')
    if move == 'drop':
        return s_move_drop(state,socket)
        
    elif move == 'pop':
        return s_move_pop(state,socket)
        
    else:
        print('Invalid move option, try again.')
        s_move_ops(state,socket)

    
def s_move_pop(state,socket):
    try:
        column = eval(input('Which column (0-6) do you want to pop? '))
    except:
        print('Invalid input')
        return s_move_pop(state,socket)
    try :
        newstate = _pop_piece(state,column)
        if state != newstate:
            state = newstate
            winner = connectfour.winning_player(state)

        mode = 'POP'
        if state.turn == 'R':
            wait_player_move(mode, column,socket)
        elif state.turn == 'Y':
            wait_server_move(mode, column,socket)
    except:
        print('\n' + str(column) + ' Not a valid column')
        s_move_ops(state,socket)
    finally:
        return state

        
def s_move_drop(state,socket):

    while True:
        column = input('Which column (0-6) do you want to drop? ')
        newstate = _drop_piece(state,column)
        if state != newstate:
            state = newstate
            winner = connectfour.winning_player(state)
            break

    mode = 'DROP'
    if state.turn == 'R':
        wait_player_move(mode, column, socket)
    elif state.turn == 'Y':
        wait_server_move(mode,column,socket)

    return state

def wait_player_move(mode, column, socket):
    I32CFP.convert_move_to_I32CFP(mode, column, socket)
    print('Waiting for player to move or update.')
  
##client
def client(state):
    connect_socket = I32CFP.client_side()
    
    print_board(state.board)
    print('R is your sign.')
    state = player_first_move(state, connect_socket)

    winner = ' '
    while winner == ' ':
        winner = makingmove(connect_socket, state, winner)
    if winner == 'R':
        print('Red won.')
    elif winner == 'Y':
        print('Yellow won.')
    I32CFP.close_socket(connect_socket)

        
def player_first_move(state, socket):
    return s_move_ops(state, socket)

def wait_server_move(mode,column,socket):
    I32CFP.convert_move_to_I32CFP(mode, column, socket)
    print('Waiting for server to move or update.')

if __name__ == '__main__':
    who_r_you()

    



























