# example_client.py
#
# ICS 32 Winter 2013
# Code Example
#
# This is an example socket client that simply connects to a particular
# address and port (in this case, port 19999 on the machine you're running
# the program on) and sends it the following text:
#
#     99 bottles of beer on the wall
#     98 bottles of beer on the wall
#     97 bottles of beer on the wall
#     ...
#     2 bottles of beer on the wall
#     1 bottles of beer on the wall
#
# (If you want a small challenge, find an elegant way to remove the
# pluralization when the number of bottles is 1.)
#
# After each line of text is sent, the program waits for 0.2 seconds
# before sending the next line.  If you run example_server.py and
# example_client.py, you'll see the lyrics come up at a rate of about
# five lines per second, so it'll take on the order of 20 seconds until
# you see the last lyric.

import socket
import time


if __name__ == '__main__':
    # We need a socket in order to connect to the server, so we'll first
    # create one.
    connect_socket = socket.socket()

    print('Connecting...')

    # Connecting a socket to another program is simple: call the
    # connect() method and pass it a two-element tuple containing
    # the IP address and port.  Note the two pairs of parentheses
    # here.  They're not for show; they mean something.  In particular,
    # they mean that what we're passing to connect() is not two parameters,
    # but really one: a tuple with two elements.
    connect_socket.connect(('127.0.0.1', 19999))

    # As in our server, since we're sending text, it'll be most convenient
    # if we can treat our socket like a text file.  So we'll call makefile
    # and ask for a pseudo-file object that lets me write to it the way I
    # write to a text file; any text I write will be sent through the socket
    # to the other program.
    connect_socket_output = connect_socket.makefile('w')

    print('Sending the song lyrics...')

    # There's one interesting thing going on here you should know about.
    # Note the call to the flush() method after each call to write().
    # Oddly enough, writing to something external -- like a file or a
    # socket -- doesn't always cause data to be immediately written.
    # This is because writing data externally is potentially quite
    # expensive.  Hard drives, for example, are hideously slow compared
    # to writing data into memory.  So instead of writing data every
    # time we ask Python to do it, Python will instead store the data
    # in a "buffer" in memory; every once in a while, when the buffer
    # gets large enough to make it worth our while, the contents of the
    # buffer will be "flushed", meaning that the data will be written
    # externally (i.e., written to the file or socket or whatever).
    #
    # That's fine if your goal is just to blast a bunch of data out.
    # But if you care that your data actually gets sent at certain
    # times -- which is very important in the context of a network
    # protocol, because you're sending commands from one program to
    # another, and you might then wait for a response, so the other
    # program had better receive the command, or there will never *be*
    # a response! -- then you have to flush the buffer manually.
    # Here, we want every line of our lyrics to show up on the server's
    # console after it's written, so we'll flush after every one of them.

    for bottles in range(99, 0, -1):
        lyric_line = '{} bottles of beer on the wall\n'.format(bottles)
        connect_socket_output.write(lyric_line)
        connect_socket_output.flush()
        time.sleep(0.2)

    print('Done!')

    # As in our server, we'll close both the pseudo-file object *and*
    # the socket when we're done.
    connect_socket_output.close()
    connect_socket.close()
