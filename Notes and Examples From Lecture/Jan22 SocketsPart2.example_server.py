# example_server.py
#
# ICS 32 Winter 2013
# Code Example
#
# This is an example socket server that waits for a single incoming
# connection from another program, accepts that connection, and continues
# reading lines of text from the other program until the other program
# closes its socket.  Any text that's read from the socket is simply
# printed to the console.

import socket


if __name__ == '__main__':
    # Create a socket and bind it to the port on which we want to wait
    # for a connection.  In this case, we're using port 19999;
    # remember that '127.0.0.1' is an IP address that always refers
    # to the current machine (whatever machine you're running this
    # program on).
    listen_socket = socket.socket()
    listen_socket.bind(('127.0.0.1', 19999))

    # Set the socket to "listen mode".
    listen_socket.listen(0)

    print('Waiting for connection...')

    # Accept a connection.  Remember that this function will "block"
    # (i.e., your program will pause, making no more progress) until
    # another program connects to it on port 19999.
    connection_socket, from_address = listen_socket.accept()

    # Now that we accepted a connection -- which gave us back another
    # socket on which we'll actually have our conversation -- we can
    # close the socket we were using to listen, since we're not
    # planning on listening for more connections.
    listen_socket.close()

    print('Connection from {} accepted'.format(from_address))

    # This is an important trick.  Here, we're asking for a sort of
    # file object, but that reads text from a socket instead of from a file.
    # Its "interface" (i.e., the set of methods it provides) is the same
    # as the one provided by a file object.
    #
    # The argument 'r' is interpreted the same way that it would be if
    # you were calling the built-in open() function: it means we intend
    # to read text.
    #
    # The result we get back from calling makefile('r') on our socket
    # is that pseudo-file object.
    connection_socket_input = connection_socket.makefile('r')

    # Now we can treat our socket more like a text file.  You could write
    # this same loop to read text from a file.  As with reading text from
    # a file, readline() will return an empty string if the other program's
    # socket is closed (i.e., it has no more text to send us).
    #
    # Notice that the print() call has an extra parameter "end=''".  This
    # is because, as when we read lines of text from a text file, the
    # strings we get back contain newline characters.  If we print strings
    # with newline characters on the end of them, there's no reason to
    # ask print() to also print a newline.
    #
    # If you don't remember what the "end" parameter does, change it to
    # this and watch what happens:
    #
    #     print(line, end='...')
    
    line = connection_socket_input.readline()

    while len(line) > 0:
        print(line, end='')
        line = connection_socket_input.readline()

    # Once there is no more data to be read from the socket, we have to
    # close *both* the pseudo-file object *and* the socket.
    connection_socket_input.close()
    connection_socket.close()
