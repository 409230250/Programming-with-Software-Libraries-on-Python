## 

import connectfour
import socket
#import i32tfsp

def connect_four():
    print('Welcom to Connect Four!')
    Start_Game = connectfour.new_game_state()
    select_game_mode(Start_Game)
    
def select_game_mode(Start_Game):
    game_mode = input('Select a game mode(C =console_only; S = as a host; J = join a game): ').lower()
    if game_mode == 'c':
        print('Mode: Console Only')
        console_only(Start_Game)
    elif game_mode == 's':
        print('Mode: Host(server)')
        as_server(Start_Game)
    elif game_mode == 'j':
        print('Mode: Client')
        as_client(Start_Game)
    else:
        select_game_mode(Start_Game)


## console only.
        
def console_only(Start_Game):
    display_board(Start_Game)
    move_ops(Start_Game)

def display_board(gamestate):
    print('0  1  2  3  4  5')
    display_list = []
    for row in gamestate.board:
        sub_list = []
        for col in row:
            if col == ' ':
                sub_list.append('.')
            else:
                sub_list.append(col)
        display_list.append(sub_list)
    for i in range(0,6):
        print('{}  {}  {}  {}  {}  {}'.format(display_list[0][i],
                                          display_list[1][i],
                                          display_list[2][i],
                                          display_list[3][i],
                                          display_list[4][i],
                                          display_list[5][i]))

def move_ops(gamestate):
    print('player {}\'s turn'.format(gamestate.turn))
    move = input('Please select a move option(p=  pop,d = drop): ')
    if move == 'd':
        return move_drop(gamestate)
    elif move == 'p':
        return move_pop(gamestate)
    else:
        print('invalide move option')
        move_ops(gamestate)
        
def move_pop(gamestate):
    try:
        pop = eval(input('please select a row(0-5): '))
    except SyntaxError:
        print('invalid input')
        return move_pop(gamestate)
    except NameError:
        print('invalid input')
        return move_pop(gamestate)
    try :
        gamestate = gamestate._replace(board = connectfour.pop_piece(gamestate, pop).board,
                                              turn= connectfour._opposite_turn(gamestate.turn))   
        display_board(gamestate)
        return move_ops(gamestate)
    except ValueError:
        print('\n' + str(drop) + ' Not avalid column')
        move_pop(gamestate)
    except connectfour.ConnectFourGameOverError:
        print('Game Over')
        print('winner: ' + connectfour.winning_player(gamestate))
        return
    except connectfour.InvalidConnectFourMoveError:
        print('Column is full')
        move_pop(gamestate)

def move_drop(gamestate):
    try:
        drop = eval(input('please select a row(0-5): '))
    except SyntaxError:
        print('invalid input')
        return move_drop(gamestate)
    except NameError:
        return move_drop(gamestate)
    try :
        gamestate = gamestate._replace(board = connectfour.drop_piece(gamestate, drop).board,
                                              turn= connectfour._opposite_turn(gamestate.turn))   
        display_board(gamestate)
        return move_ops(gamestate)
    except ValueError:
        print('\n' + str(drop) + ' Not avalid column')
        move_drop(gamestate)
    except connectfour.ConnectFourGameOverError:
        print('Game Over')
        print('winner: ' + connectfour.winning_player(gamestate))
        return
    except connectfour.InvalidConnectFourMoveError:
        print('you can only pop your own peice')
        move_drop(gamestate)
##############################################
## Connect Four Network Gameplay
################################################
## Play as server   #######################
def as_server(Start_Game):
    try:
        address = input('Enter your IP address: ')
        port = eval(input('Enter a port number(1024-63553): '))
        display_board(Start_Game)
        get_connection(address,port,Start_Game)
    except SyntaxError:
        print('Invalid input. Try again.')

def get_connection(address,port,Start_Game):
    listen_socket = socket.socket()
    listen_address = (address, int(port))
    try:
        listen_socket.bind(listen_address)
        pass
    except:
        print('Error. Invalid address.')
        as_server(Start_Game)
    listen_socket.listen(0)
    print('Connection pending...')
    connection_soc, address = listen_socket.accept()
    print('{} is connected!'.format(address))
    listen_socket.close()
    receive_protocols(connection_soc)
    print('waiting for player to move.')
    winning_player = connectfour.winning_player(Start_Game)
    while winning_player == connectfour.winning_player(Start_Game) :
        file_in = connection_soc.makefile('r')
        move_info = file_in.readline()
        print('this is move info:' + move_info)
        file_in.close()
        if len(move_info)== 0:
            break
        else:
            server_game(Start_Game,move_info,connection_soc)
    
    print('game over')
    
    connection_soc.close()
    return 
    
def server_game(Start_Game,move_info, socket):
    player_game_state = convert_gamestate(Start_Game,move_info)
    display_board(player_game_state)
    winning_player = connectfour.winning_player(Start_Game)
    s_move_ops(player_game_state, socket)
    pass
    

def convert_gamestate(Start_Game,move_info):
    move_info = move_info.split(' ')
    if move_info[0] == 'DROP':
        return auto_drop(Start_Game,move_info[1])
    elif move_info[0] == 'POP':
        return auto_pop(Start_Game,move_info[1])

def auto_drop(gamestate, col):
    gamestate = gamestate._replace(board = connectfour.drop_piece(gamestate, int(col)).board,
                                              turn= connectfour._opposite_turn(gamestate.turn)) 
    return gamestate

def auto_pop(gamestate, col):
    gamestate = gamestate._replace(board = connectfour.pop_piece(gamestate, int(col)).board,
                                              turn= connectfour._opposite_turn(gamestate.turn)) 
    return gamestate
    
def receive_protocols(socket):
    file_in = socket.makefile('r')
    protocols = file_in.readline()
    file_in.close()
    if protocols == 'I32CFP_HELLO\n':
        file_out = socket.makefile('w')
        file_out.write('READY\n')
        file_out.flush()
        file_out.close()
        pass
    else:
        socket.close()
        print('Client is not speaking the same protocols.Closing connection.\n')
        return 
    
    
def wait_player_move(mode, col,socket):
    output = socket.makefile('w')
    output.write(mode+ ' ' + str(col)+'\n')
    output.flush()
    output.close()
    print('waiting for player to move')
    pass
################################################################
##   game move options!!!#############
def s_move_ops(gamestate,socket):
    print('player {}\'s turn'.format(gamestate.turn))
    move = input('Please select a move option(p=  pop,d = drop): ')
    if move == 'd':
        return s_move_drop(gamestate,socket)
    elif move == 'p':
        return s_move_pop(gamestate,socket)
    else:
        print('invalide move option')
        s_move_ops(gamestate,socket)
        
def s_move_pop(gamestate,socket):
    try:
        pop = eval(input('please select a row(0-5): '))
    except SyntaxError:
        print('invalid input')
        return s_move_pop(gamestate,socket)
    except NameError:
        print('invalid input')
        return s_move_pop(gamestate,socket)
    try :
        gamestate = gamestate._replace(board = connectfour.pop_piece(gamestate, pop).board,
                                              turn= connectfour._opposite_turn(gamestate.turn))   
        display_board(gamestate)
        mode = 'POP'
        if gamestate.turn == 'R':
            wait_player_move(mode, pop,socket)
        elif gamestate.turn == 'Y':
            wait_server_move(mode, pop,socket)
    except ValueError:
        print('\n' + str(pop) + ' Not avalid column')
        s_move_pop(gamestate,socket)
    except connectfour.ConnectFourGameOverError:
        pass
    except connectfour.InvalidConnectFourMoveError:
        print('not a valid move. cannot pop other player\'s peice and you cannot pop empty columns\n')
        s_move_pop(gamestate,socket)

        
def s_move_drop(gamestate,socket):
    try:
        drop = eval(input('please select a row(0-5): '))
    except SyntaxError:
        print('invalid input')
        return s_move_drop(gamestate,socket)
    except NameError:
        return s_move_drop(gamestate,socket)
    try :
        gamestate = gamestate._replace(board = connectfour.drop_piece(gamestate, drop).board,
                                              turn= connectfour._opposite_turn(gamestate.turn))   
        display_board(gamestate)
        print('runs drop')
        mode = 'DROP'
        if gamestate.turn == 'R':
            print('2working?')
            wait_player_move(mode, drop,socket)
        elif gamestate.turn == 'Y':
            print('working?')
            print(drop)
            wait_server_move(mode,drop,socket)
    except ValueError:
        print('\n' + str(drop) + ' Not avalid column')
        s_move_drop(gamestate,socket)
    except connectfour.ConnectFourGameOverError:
        pass
    except connectfour.InvalidConnectFourMoveError:
        print('you can only pop your own peice')
        s_move_drop(gamestate,socket)
###############################################################

## client side    ###########################

def as_client(Start_Game):
    address = input('Enter your servers address: ')
    port = eval(input('Enter a server\'s port number(1024-63553): '))
    display_board(Start_Game)
    client_to_server(address,port,Start_Game)

def client_to_server(address,port,Start_Game):
    server_socket = socket.socket()
    try:
        print('This is the address and port: ', address, ':', port)
        server_socket.connect((address,int(port)))
        print('Connecting...')
        client_protocol(server_socket)# check this function
        player_first_move(Start_Game,server_socket)
        winning_player = connectfour.winning_player(Start_Game)
        while winning_player == connectfour.winning_player(Start_Game) :
            file_in = server_socket.makefile('r')
            move_info = file_in.readline()
            print('this move info ' + move_info)
            file_in.close()
            if len(move_info)== 0:
                break
            else:
                gamestate = Start_Game._replace(turn= connectfour._opposite_turn(Start_Game.turn))
                client_game(gamestate,move_info,server_socket)
    
    except:
        print('Unable to connect.')
        as_client(Start_Game)
        
    finally:
        server_socket.close()
        print('Game Over')
        
def player_first_move(Start_Game, socket):
    return s_move_ops(Start_Game, socket)

def client_game(Start_Game,move_info,socket):
    gamestate = convert_gamestate(Start_Game,move_info)
    display_board(gamestate)
    return s_move_ops(gamestate,socket)

def wait_server_move(mode,drop,socket):
    print('runing wait server move')
    output = socket.makefile('w')
    output.write(mode+ ' ' + str(drop)+'\n')
    output.flush()
    output.close()
    print('waiting for server to move')
    pass

def client_protocol(socket):
    connect_write_to_server = socket.makefile('w')
    protocol = 'I32CFP_HELLO\n'
    connect_write_to_server.write(protocol)
    connect_write_to_server.flush()
    receive_ready = socket.makefile('r')
    protocol = receive_ready.readline()
    if protocol == 'READY\n':
        print('The server is ready to start the game')
        pass
    else:
        socket.close()
        print('server not speaking the same protocols,close connection.\n')
        return 

## Start Program
if __name__ == '__main__':
    
    connect_four()



    
## If server is not responding
    ## give it a time limit
    ## ask user if tey want to quit

## if serveris disconnected
    ## ask the user if they want to reconnect
    ## saves current game state if possible

## 
    
    
   

    
    
