# text_file_server.py
#
# ICS 32 Winter 2013
# Code Example
#
# A quick and dirty server that receives a text file using the I32TFSP protocol.

import i32tfsp



if __name__ == '__main__':
    listen_port = int(input('Listen port: '))

    print('Waiting for connection...')

    i32tfsp.receive_file(listen_port)
