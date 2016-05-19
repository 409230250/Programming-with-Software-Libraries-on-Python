# text_file_client.py
#
# ICS 32 Winter 2013
# Code Example
#
# A quick and dirty client that sends a text file using the I32TFSP protocol.
# This is a little bit more full-featured than our example from lecture, as
# it asks the user to specify the file to be sent and where to send it.
# There's no error handling on the user's input, so exercise some care
# in using it.
#
# In short, there's nothing here we haven't seen before, *except* that you'll
# notice that we're importing our own i32tfsp module here and calling its
# functions.
#
# Modules are modules in Python, and our modules are on a level field with
# the ones in the Python Standard Library.  We import our modules the same
# way and we call the functions the same way (by qualifying them with the
# name of the module).  The only tricky part is setting them up so that
# Python can find them, the simplest solution to which is to put all of
# the modules comprising a program into the same directory.

import i32tfsp



if __name__ == '__main__':
    print('What do you want to send?')
    file_to_send = input('File to send: ')
    description = input('Description: ')

    print('Where do you want to send it?')
    host = input('Host: ')
    port = int(input('Port number: '))
    
    i32tfsp.send_file(host, port, file_to_send, description)
