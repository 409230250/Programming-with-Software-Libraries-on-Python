

#Peter Thai () and Junjie Lin (25792830) 
import connectfour
import socket

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
        print("Error. Which column (0-6) do you want to drop?")
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
##print_board(drop_piece(drop_piece(new_game_state(),4),0).board)

##server
def server(state):
    try: 
        port = input ('Please enter a port number: ')
        listen_socket = socket.socket()
        listen_address = ('', int(port))
    
        listen_socket.bind(listen_address)

        listen_socket.listen(0)
    except:
        print('ValueError, please try again.')
        server(state)
    print('Waiting for connection...')

    stream_socket, from_address = listen_socket.accept()
    print('Connection with {}'.format(from_address))
    listen_socket.close()
    
    connection_socket_input = stream_socket.makefile('r')
    line = connection_socket_input.readline()
    connection_socket_input.close()
        
    if line == 'I32CPF_HELLO\n':
        connection_socket_output = stream_socket.makefile('w')
        connection_socket_output.write('READY\n')
        connection_socket_output.flush()
        connection_socket_output.close()
    else:
        connection_socket.close()
        print('Client is not ready.Closing connection.\n')
        return
    
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
    stream_socket.close()
        
def makingmove(stream_socket,state, winner):
        line = stream_socket.makefile('r')
        line_in = line.readline()
        line.close()

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
        print('Invalide move option, try again.')
        s_move_ops(state,socket)

    
def s_move_pop(state,socket):
    try:
        column = eval(input('Which column (0-6) do you want to drop? '))
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
        print('\n' + str(column) + ' Not avalid column')
        s_move_ops(state,socket)
    finally:
        return state

        
def s_move_drop(state,socket):
    try:
        column = eval(input('Which column (0-6) do you want to drop? '))
    
        newstate = _drop_piece(state,column)
        if state != newstate:
            state = newstate
            winner = connectfour.winning_player(state)

        mode = 'DROP'
        if state.turn == 'R':
            wait_player_move(mode, column, socket)
        elif state.turn == 'Y':
            wait_server_move(mode,column,socket)
    finally:
        return state

def wait_player_move(mode, column, socket):
    output = socket.makefile('w')
    output.write(mode+ ' ' + str(column)+'\n')
    output.flush()
    output.close()
    print('Waiting for player to move or update.')
  
##client
def client(state):
    address = input('Please enter the address of your server: ')
    port = input ('Please enter the port of your server: ')
    print('Checking the connection.')
    connect_socket = socket.socket()
    try:
        connect_socket.connect((address,int(port)))
        print('Done! Connecting with (', address, ':', port,')')
    except:
        print('Wrong address or port (', address, ':', port, '), please try again.')
        client(state)
    connect_socket_output = connect_socket.makefile('w')
    connect_socket_output.write('I32CPF_HELLO\n')
    connect_socket_output.flush()
    connect_socket_output.close()
    
    connect_socket_input = connect_socket.makefile('r')
    line = connect_socket_input.readline()
    if line == 'READY\n':
        print('Game starts.')  
    else:
        connect_socket.close()
        print('The protocol does not match, close connection.\n')
        return
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
    connect_socket.close()
        
def player_first_move(state, socket):
    return s_move_ops(state, socket)

def wait_server_move(mode,column,socket):
    output = socket.makefile('w')
    output.write(mode+ ' ' + str(column)+'\n')
    output.flush()
    output.close()
    print('Waiting for server to move or update.')

if __name__ == '__main__':
    who_r_you()

    



























