# i32tfsp.py
#
# ICS 32 Winter 2013
# Code Example
#
# This module implements the I32TFSP protocol.  However, it contains no
# user interface and is not a "program" that can be executed; it provides
# utility functions that can be used by programs, in the same way that
# modules like "os" and "socket" do in the Python Standard Library.
# It's fair to say, actually, that this module is a small library.  (See?
# We can build libraries, too!)

import collections
import socket



# When there are protocol-related errors (i.e., one party in an I32TFSP
# session does not behave correctly according to the protocol), we will
# raise this exception.
class I32TfspError(Exception):
    pass



# We spoke in lecture about the design of this module and came to the
# conclusion that the main utilities you really want to provide to other
# modules (e.g., a user interface) is the ability to send a file and the
# ability to receive one.  I32TFSP itself is just a means to that end,
# and it's best to hide all of that detail within the module.  A program
# shouldn't have to know all about what messages are sent back and forth
# over the socket in order to make the communication happen; it should
# simply be able to say "I want to send this file there" or "I want to
# receive a file".
#
# For that reason, all of the protocol-specific behavior is actually
# isolated in private functions (with names beginning with underscores).




# Having isolated the specifics of the socket and protocol behavior
# in other functions, this function becomes shorter, simpler, and
# much clearer.  What does this function do?  It initiates a connection,
# tries to send a "hello", then receive a "hi"; either way, no matter
# what, it closes the connection on the way out.
#
# This is one of the big benefits of breaking larger functions into
# smaller ones.  Do you notice how the comment above tells you almost
# nothing you couldn't figure out by looking at the code?  Code that
# reads more like it's written in natural language can be a lot more
# readable than the alternative.
#
# Notice that _initiate_connection() returns a "connection" object that
# is then sent to other functions subsequently.  From the point of view
# of this function, that connection object is opaque.  The details of
# what's in that function show up in the private area of the module below.
def send_file(host, port, file_path, description):
    '''Given a host (the IP address or name of a machine), a port number,
    the path to a file on this computer, and a description of that file,
    this function uses the I32TFSP protocol to offer it and, if accepted,
    send it to another party.'''

    connection = _initiate_connection(host, port)

    try:
        _send_hello(connection)
        _receive_hi(connection)
    finally:
        _close_connection(connection)



def receive_file(port):
    '''Given a port number, this function waits for a connection that port
    and then uses the I32TFP protocol to receive it.'''

    connection = _accept_connection(port)

    try:
        _receive_hello(connection)
        _send_hi(connection)
    finally:
        _close_connection(connection)



# You'll notice that we haven't finished our protocol implementation yet.
# For the time being, we've only exchanged pleasantries ("Hello!"  "Hi!")
# But most of the concepts required to send and receive messages back and
# forth have been dealt with already; a lot of what's left is detail.
# There are a couple of wrinkles, and we'll see them in the next lecture,
# but this is a very good start.



# And now we reach a set of private definitions in our module, the things
# that are hidden implementation details that do not need to be used from
# other modules.



# This is the connection object we saw in the send_file() and receive_file()
# functions above.  We discovered that we needed to know three things about
# a connection at any given time:
#
# (1) The socket across which the connection is traveling
# (2) A pseudo-file object that lets us read input from that socket as
#     though we were reading from a text file
# (3) A pseudo-file object that lets us write input to that socket as
#     though we were writing to a text file

_I32TfspConnection = collections.namedtuple(
    '_I32TfspConnection', ['socket', 'socket_input', 'socket_output'])



# The next three functions initiate and accept connections.  Essentially
# everything happening here uses raw materials (socket.socket(),
# socket.connect(), socket.accept(), socket.makefile()) that we've seen
# in previous code examples.


def _initiate_connection(host, port):
    '''Given a host and a port, this function initiates a connection and
    returns an _I32TfspConnection object describing that connection.
    This function may raise exceptions related to socket connectivity
    if, for example, the attempt to connect fails.'''
    connect_socket = socket.socket()
    connect_socket.connect((host, port))

    # This is a change we didn't make in lecture.  I observed that
    # both _initiate_connection() and _accept_connection() needed to
    # do the same task: take the connection's socket and build an
    # _I32TfspConnection namedtuple from it.  So I turned that into a
    # function, so I wouldn't have to write the code in two places.
    return _build_connection_object(connect_socket)



def _accept_connection(port):
    '''Given a port number, this functions waits for a connection to
    arrive on that port.  It then builds an _I32TfspConnection object
    describing that connection.'''
    listen_socket = socket.socket()
    listen_socket.bind(('127.0.0.1', port))
    listen_socket.listen(0)

    connect_socket, from_address = listen_socket.accept()

    listen_socket.close()

    return _build_connection_object(connect_socket)



def _build_connection_object(connect_socket):
    '''Takes a socket and builds an _I32TfspConnection namedtuple from it.'''
    connect_socket_input = connect_socket.makefile('r')
    connect_socket_output = connect_socket.makefile('w')

    return _I32TfspConnection(
        socket=connect_socket, socket_input=connect_socket_input,
        socket_output=connect_socket_output)



def _close_connection(connection):
    '''Closes a connection.'''

    # We've seen previously that closing a socket also requires closing
    # any pseudo-file objects created from it.  Isolating the solution
    # to that problem here prevents us from forgetting it in other places;
    # if we need to close a connection, we just call this function and
    # everything is handled.
    connection.socket_input.close()
    connection.socket_output.close()
    connection.socket.close()



def _send_hello(connection):
    '''Sends an I32TFSP_HELLO message'''
    connection.socket_output.write('I32TFSP_HELLO\n')
    connection.socket_output.flush()



def _receive_hello(connection):
    '''Receives an I32TFSP_HELLO message, raising an I32TfspError if anything
    other than that is received'''
    if connection.socket_input.readline() != 'I32TFSP_HELLO\n':
        raise I32TfspError()



def _send_hi(connection):
    '''Sends an I32TFSP_HI message'''
    connection.socket_output.write('I32TFSP_HI\n')
    connection.socket_output.flush()



def _receive_hi(connection):
    '''Receives an I32TFSP_HI message, raising an I32TfspError if anything
    other than that is received'''
    if connection.socket_input.readline() != 'I32TFSP_HI\n':
        raise I32TfspError()



# Food for thought: Don't _send_hello() and _send_hi() look like pretty
# much the same function?  And _receive_hello() and _receive_hi() likewise?
# Think about a way to solve that problem, so that the things that make each
# pair of functions similar is isolated in a separate function.
