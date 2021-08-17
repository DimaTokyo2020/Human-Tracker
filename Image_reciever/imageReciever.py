#!/usr/bin/env python

import random
import socket, select
from time import gmtime, strftime
from random import randint

imgcounter = 1
basename = "image%s.png"

HOST = '192.168.1.100'
PORT = 1818

connected_clients_sockets = []

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))
server_socket.listen(10)

connected_clients_sockets.append(server_socket)
buffer_size = 469766
#buffer_size2 = 

while True:
    print('statr')
    read_sockets, write_sockets, error_sockets = select.select(connected_clients_sockets, [], [])



    for sock in read_sockets:

        if sock == server_socket:

            sockfd, client_address = server_socket.accept()
            connected_clients_sockets.append(sockfd)

        else:
            try:
                #print('Buffer size is %s' % buffer_size)
                
                data_size = sock.recv(buffer_size)
                print('got data: ')
                file_size = int(data_size.decode('utf-8')[2:])
                print('the size is : ' + str(file_size))

                data = sock.recv(buffer_size)
                print('dtat dima: ' + str(data))
                #8324457
                continueLoop = True
                while continueLoop:
                 data += sock.recv(buffer_size)  
                 print('len: ' + str(len(data)))          
                 if len(data) == file_size:
                  print('break')
                  continueLoop = False       
                print('After loop')
                txt = 'dima'
                len(data)
                print('len: ' + str(len(data)))

		 #print('len data: ' + str('dima'))
#                txt = data.decode('utf8')
 #               print('len: ' + str(len(txt)))
  #              print('text : ' + txt)
		 

                if txt.startswith('SIZE'):
                    tmp = txt.split()
                    size = int(tmp[1])

                    print ('got size')
                    print ('size is %s' % size)

                    sock.send("GOT SIZE")
                    # Now set the buffer size for the image 
                    buffer_size = 40960000

                elif txt.startswith('BYE'):
                    sock.shutdown()

                elif data:
                    print('open file')
                    myfile = open(basename % imgcounter, 'wb')

                    # data = sock.recv(buffer_size)
                    if not data:
                        myfile.close()
                        print('error')
                        break
                    myfile.write(data)
                    print('saved ')
                    myfile.close()
                    print('saved2 ')
                    sock.send("GOT IMAGE")
                    buffer_size = 469766
                    sock.shutdown()
                    print('saved3 ')
            except Exception as e:
                print(e)
                sock.close()
                connected_clients_sockets.remove(sock)
                continue
        imgcounter += 1
server_socket.close() 







def stop():
    time.sleep(10) 
    




