# example_server.py
#
# ICS 32 Winter 2013
# Code Example
#
# This is a simple example of a Python socket server.  It waits for one
# incoming connection on port 19999, then prints whatever is sent from
# the other program to its console.  When there is no more data from the
# other program, the program ends.

import socket


if __name__ == '__main__':
    # Create a new socket object.
    listen_socket = socket.socket()

    # Bind the socket to port 19999 on this machine and prepare to
    # listen on the socket.
    listen_address = ('127.0.0.1', 19999)
    listen_socket.bind(listen_address)
    listen_socket.listen(0)
    
    print('Waiting for connection...')

    # At this point, wait until an incoming connection arrives;
    # we'll get back a fresh socket on which to have a conversation,
    # along with the address of the machine that connected to us.
    stream_socket, from_address = listen_socket.accept()

    # Since we're only aiming to listen for one connection, we'll
    # close the listen socket, as we're done with it.
    listen_socket.close()
    
    print('Connection from {}'.format(from_address))

    # You'll quite often see a loop used to read from a socket, because
    # you can never be sure you'll get as much data as you ask for.
    # Here, we're asking for 4096 bytes at a time, but we might get
    # anywhere from 1 to 4096 bytes, depending on a variety of factors.
    while True:
        # Attempt to read up to 4096 bytes
        incoming_bytes = stream_socket.recv(4096)

        # If we got no bytes at all, that means the other side has
        # specified that it's done writing to its socket.
        # Otherwise, we'll convert the bytes to a string and print
        # them to the console.
        if len(incoming_bytes) == 0:
            print('Connection from {} closed'.format(from_address))
            break
        else:
            # The decode() method on a bytes object is how you convert
            # bytes to a string.  Since we won't necessarily read one
            # line of input at a time, and since newline characters will
            # be part of what's sent from the other computer, we'll ask
            # the print() function to leave the newlines out.
            print(incoming_bytes.decode(encoding='utf-8'), end='')

    # Since we've read all the data that's been sent, we're done;
    # close the connection and end the program.
    stream_socket.close()
