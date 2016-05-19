
#Peter Thai (66218086) and Junjie Lin (25792830)
import socket

#### Server
def server_side():

    stream_socket, from_address = _listening_socket()

    _server_I32CPF_check(stream_socket)
    return stream_socket, from_address
    

def _listening_socket():
    try:
        port = input('Please enter a port number: ')
        listen_socket = socket.socket()
        listen_address = ('', int(port))
        listen_socket.bind(listen_address)
        listen_socket.listen(0)
    except:
        print("ValueError, please try again.")
        return _listening_socket()
        
    print('Waiting for connection...')
    stream_socket, from_address = listen_socket.accept()
    print('Connection with {}'.format(from_address))
    listen_socket.close()
    return stream_socket, from_address

def _server_I32CPF_check(stream_socket):
    connection_socket_input = stream_socket.makefile('r')
    line = connection_socket_input.readline()
    connection_socket_input.close()
    _servercheck_hello(stream_socket, line)
    
def _servercheck_hello(stream_socket, line):
    if line == 'I32CPF_HELLO\n':
        connection_socket_output = stream_socket.makefile('w')
        connection_socket_output.write('READY\n')
        connection_socket_output.flush()
        connection_socket_output.close()
    else:
        stream_socket.close()
        print('Client is not ready.  Closing connection.\n')
        return

### client
def client_side():

    connect_socket = _calling_socket()
        
    _sending_hello(connect_socket)
    _receiving_ready(connect_socket)
    return connect_socket

def _calling_socket():
    address = input('Please enter the address of your server: ')
    port = input ('Please enter the port of your server: ')
    print('Checking the connection.')
    connect_socket = socket.socket()

    try:
        connect_socket.connect((address,int(port)))
        print('Done! Connecting with (', address, ':', port,')')
    except:
        print('Wrong address or port (', address, ':', port, '), please try again.')
        return _calling_socket()

    return connect_socket

def _sending_hello(connect_socket):
    connect_socket_output = connect_socket.makefile('w')
    connect_socket_output.write('I32CPF_HELLO\n')
    connect_socket_output.flush()
    connect_socket_output.close()

def _receiving_ready(connect_socket):
    connect_socket_input = connect_socket.makefile('r')
    line = connect_socket_input.readline()
    if line == 'READY\n':
        print('Game starts.')  
    else:
        connect_socket.close()
        print('The protocol does not match, close connection.\n')
        return

    
### other network and protocol items
def read_move(stream_socket):
    line = stream_socket.makefile('r')
    line_in = line.readline()
    line.close()
    return line_in

def close_socket(socket):
    socket.close()

def convert_move_to_I32CFP(mode, column, socket):
    output = socket.makefile('w')
    output.write(mode+ ' ' + str(column)+'\n')
    output.flush()
    output.close()
