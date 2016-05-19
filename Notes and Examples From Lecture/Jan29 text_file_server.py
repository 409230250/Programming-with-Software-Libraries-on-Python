# text_file_server.py
#
# ICS 32 Winter 2013
# Code Example
#
# A quick and dirty server that receives a text file using the I32TFSP protocol.
# This has been modified slightly from the previous version, because the
# i32tfsp.receive_file function now takes additional parameters:
# a "receive directory" specifying where received files should be written,
# and an "accept file function" specifying what should be done when the
# protocol has to either accept or reject the file (in this case, we're
# asking the user).

import i32tfsp



def ask_user_to_accept_file(filename, description):
    print('A file has been offered')
    print('Filename: ' + filename)
    print('Description: ' + description)

    return input('Accept the file?  [Y]es or [N]o? ').strip().upper().startswith('Y')



if __name__ == '__main__':
    listen_port = int(input('Listen port: '))
    receive_directory = input('Receive directory: ')

    print('Waiting for connection...')

    i32tfsp.receive_file(listen_port, receive_directory, ask_user_to_accept_file)
