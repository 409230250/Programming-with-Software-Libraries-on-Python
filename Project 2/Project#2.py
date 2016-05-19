import connectfour
import socket


def who_r_you():
    modul=input('please enter what modul you want to play as: ')
    if modul == 's':
        return server()
    elif modul == 'c':
        return client()
    elif modul == 'con':
        return console()

def console():
    state = connectfour.new_game_state()
    winner = ' '
    print_board(state.board)
    while winner == ' ':
        
        drop_or_pop = input('It\'s ' + state.turn +' turn. Please enter either drop or pop: ')

        while drop_or_pop == 'drop':
            column = input('Please enter one number from 0 to 6 for the column you want to drop: ')
            newstate = _drop_piece(state,column)
            if state != newstate:
                state = newstate
                winner = connectfour.winning_player(state)
                break

        while drop_or_pop == 'pop':
            try:
                column = input('Please enter one number from 0 to 6 for the column you want to pop: ')
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
            print('Error. Please enter either drop or pop.')
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
        print("Error. Please enter one number from 0 to 6 for column that you want to drop.")
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
def server():
    try:
        address = input ('Enter your IP address: ')
        port = input ('Enter a port number: ')
        print_board(state.board)
    listen_socket = socket.socket()
    listen_address = ('127.0.0.1', 19998)
    listen_socket.bind(listen_address)
    listen_socket.listen(0)
    
    print('Waiting for connection...')

    stream_socket, from_address = listen_socket.accept()

    listen_socket.close()
    
    print('Connection from {}'.format(from_address))
    
    connection_socket_input = stream_socket.makefile('r')
    connection_socket_output = stream_socket.makefile('w')

    line = connection_socket_input.readline()

    if line == 'I32CPF_HELLO\n':
        connection_socket_output.write('READY')
        connection_socket_output.flush()
        


    connection_socket_input.close()
    connection_socket_output.close()
    listen_socket.close()






    
##client
    

def client():
    connect_socket = socket.socket
    ()
    
    connect_socket.connect(('127.0.0.1',19998))
    
    print('Done! Connecting...')

    connect_socket_input = connect_socket.makefile('r')
    connect_socket_output = connect_socket.makefile('w')

    connect_socket_output.write('I32CPF_HELLO\n')
    connect_socket_output.flush()
    connect_socket_output.close()

    print('check, pass this step.')
    line = connect_socket_input.readline()
    if line == 'READY\n':
        print('Game starts.')
        main()
        


    connect_socket_input.close()
    connect_socket_output.close()
    connect_socket.close()
    

if __name__ == '__main__':
    who_r_you()

    



























