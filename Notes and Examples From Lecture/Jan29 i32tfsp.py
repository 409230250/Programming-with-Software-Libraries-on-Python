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
import os.path
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

        # os.path.basename takes a file's path and returns the name of the
        # file without the directory (e.g., if you give it the path
        # "/i/am/happy/today.txt', it returns 'today.txt').
        _send_filename_and_description(
            connection, os.path.basename(file_path), description)

        if _receive_yes_or_no(connection):
            _send_file_contents(connection, file_path)
            _receive_got_it(connection)
    finally:
        _close_connection(connection)



def receive_file(port, receive_directory, accept_file_function):
    '''Given a port number, a directory in which to store the received
    file, and a function that determines whether a file is
    acceptable (given its filename and description), this function waits for
    a connection on that port and then uses the I32TFP protocol to receive it,
    accepting it or rejecting it on the basis of the result returned from
    the accept_file_function.'''

    connection = _accept_connection(port)

    try:
        _receive_hello(connection)
        _send_hi(connection)

        # This is called "sequence assignment".  We're calling a function
        # that returns a tuple containing two elements.  We can assign the
        # result into two variables, in which case the tuple will be broken
        # apart, with each of the its elements assigned to one of our
        # variables.
        filename, description = _receive_filename_and_description(connection)

        if accept_file_function(filename, description):
            _send_yes(connection)
            _receive_file_contents(connection, os.path.join(receive_directory, filename))
            _send_got_it(connection)
        else:
            _send_no(connection)
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

    # This line has changed since the previous version.  We're now
    # binding to our chosen port on all network interfaces, instead
    # of only on the loopback interface.
    listen_socket.bind(('', port))

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



# We added these two functions to isolate the code used to read and write
# individual lines to our connection, which would otherwise be repeated
# in a number of places, leading to the possibility of us messing it up
# in some of those places.

def _readline_from_connection(connection):
    # Not only will we read a line of input from the connection, but we'll
    # strip the newline character from the end of it.  readline() always
    # returns a line of text followed by a newline character, so we can
    # safely strip the last character using the "slice" notation, which
    # strings support.
    return connection.socket_input.readline()[:-1]



def _writeline_to_connection(connection, line):
    # Here, we'll append a newline before writing, and we'll also remember
    # to flush.  That way, I won't have to remember to do those two things
    # everywhere else.
    connection.socket_output.write(line + '\n')
    connection.socket_output.flush()



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



# We added this function to the mix, as well.  It is used in all of the
# places where I expect to see a certain message (e.g., _receive_hello).
# Otherwise, I'd write this same "if" statement and raise the same
# exception in all of those different places.
def _expect_to_receive_message(connection, expected_message):
    '''Reads a line of input from the connection and checks whether it is
    the text that was expected.  If so, there is no effect other than the
    line of input being consumed; if not, an I32TfspError is raised to
    indicate failure.'''
    if _readline_from_connection(connection) != expected_message:
        raise I32TfspError()


def _expect_to_receive_message_with_parameter(connection, expected_message):
    '''Reads a line of input from the connection and checks whether it
    starts with the text that was expected.  If so, it returns the remainder
    of the message; if not, a I32TfspError is raised to indicate failure.
    So, for example, if expected_message is 'FILE' and the line read from
    the connection is 'FILE hello.boo', this function will return 'hello.boo'.'''
    line = _readline_from_connection(connection)

    if line.startswith(expected_message) and len(line) > len(expected_message) + 1:
        return line[len(expected_message)+1:]
    else:
        raise I32TfspError()



def _send_hello(connection):
    '''Sends an I32TFSP_HELLO message'''
    _writeline_to_connection(connection, 'I32TFSP_HELLO')



def _receive_hello(connection):
    '''Receives an I32TFSP_HELLO message, raising an I32TfspError if anything
    other than that is received'''
    _expect_to_receive_message(connection, 'I32TFSP_HELLO')



def _send_hi(connection):
    '''Sends an I32TFSP_HI message'''
    _writeline_to_connection(connection, 'I32TFSP_HI')



def _receive_hi(connection):
    '''Receives an I32TFSP_HI message, raising an I32TfspError if anything
    other than that is received'''
    _expect_to_receive_message(connection, 'I32TFSP_HI')



def _send_filename_and_description(connection, filename, description):
    '''Sends the filename and description'''
    _writeline_to_connection(connection, 'FILE ' + filename)
    _writeline_to_connection(connection, 'DESCRIPTION ' + description)



def _receive_filename_and_description(connection):
    '''Receives the filename and description and returns a tuple where
    the first element is the filename and the second element is the
    description'''
    filename = _expect_to_receive_message_with_parameter(connection, 'FILE')
    description = _expect_to_receive_message_with_parameter(connection, 'DESCRIPTION')
    return filename, description



def _send_yes(connection):
    '''Sends a YES message'''
    _writeline_to_connection(connection, 'YES')



def _send_no(connection):
    '''Sends a NO message'''
    _writeline_to_connection(connection, 'NO')



def _receive_yes_or_no(connection):
    '''Receives either a YES or a NO message.  If YES is received, this
    function returns True; if NO is received, this function returns
    False; if any other message is received, this function raises an
    I32TfspError.'''
    line = _readline_from_connection(connection)

    if line == 'YES':
        return True
    elif line == 'NO':
        return False
    else:
        raise I32TfspError()



def _send_file_contents(connection, file_path):
    file_input = open(file_path, 'r')

    try:
        file_lines = file_input.readlines()

        _writeline_to_connection(connection, 'LINES {}'.format(len(file_lines)))

        for line in file_lines:
            # The lines we read from the file will have newline characters
            # on the end of them, but we'll need to strip these out, since
            # our _writeline_to_connection function puts them back in.
            _writeline_to_connection(connection, line[:-1])

        _writeline_to_connection(connection, 'END')

    finally:
        file_input.close()



def _receive_file_contents(connection, file_path):
    file_output = open(file_path, 'w')

    try:
        line_count = int(_expect_to_receive_message_with_parameter(connection, 'LINES'))

        for i in range(line_count):
            # The lines we read from our connection don't end with newlines
            # because our _readline_from_connection() function strips them
            # out, but we'll need to make sure we write newlines to the file.
            file_output.write(_readline_from_connection(connection) + '\n')

        _expect_to_receive_message(connection, 'END')
        _send_got_it(connection)
        
    except ValueError:
        # If we get a message 'LINES ' that isn't followed by a number as the
        # protocol requires, raise an exception
        raise I32TfspError()

    finally:
        file_output.close()



def _send_got_it(connection):
    _writeline_to_connection(connection, 'GOT_IT')



def _receive_got_it(connection):
    _expect_to_receive_message(connection, 'GOT_IT')
