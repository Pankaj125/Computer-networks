import socket
import time
from tkinter import N

IP = 'localhost'
PORT = 8080
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))
recived_f = 'htdocs'+str(time.time()).split('.')[0]+'.txt'
with open(recived_f, 'wb') as f:
    print('The file has been opened')
    while True:
        #print('receiving data...')
        data = s.recv(BUFFER_SIZE)
        print('Content=%s', (data))
        if not data:
            f.close()
            print('File is succesfully closed')
            break
        # write data to a file
        f.write(data)

print('Downloaded the file successfully')
s.close()
print('Connection is now closed succesfully')