
import socket
import time,sys

# IP addr and port no.
IP = '0.0.0.0'
PORT = 8080

# Start creating a socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind((IP, PORT))
sock.listen(1)
#sock.bind('tcp://*:9999')
print('Running on the Port Number: %s ...' % PORT)

while True:    
    # Wait for client connections to establish.
    conn, addr = sock.accept()

    # Obtain the client's request
    req = conn.recv(1024).decode()
    print(req)
    

    # socket closing
    sock.close()

    # HTTP headers must be parsed.
    Head = req.split('\n')
    Name_of_file = Head[0].split()[1]

    print (Name_of_file)

    # Obtain the file's content.
    if Name_of_file == '/':
        Name_of_file = '/index.html'

    try:
        fin = open('htdocs' + Name_of_file)
        data = fin.read()
        fin.close()

        reply = 'HTTP/1.0 200 OK\n\n' + data
    except FileNotFoundError:

        reply = 'HTTP/1.0 404 NOT FOUND\n\nFile Not Found'

    # Sending the HTTP response
    conn.sendall(reply.encode())
    conn.close()
