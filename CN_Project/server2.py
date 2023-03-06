import socket
from threading import Thread

IP = 'localhost'
PORT = 8080
BUFFER_SIZE = 1024


class ClientThread(Thread):

    def __init__(self, ip, Port, socket):
        Thread.__init__(self)
        self.ip = ip
        self.Port = Port
        self.socket = socket
        print(" Starting new thread for "+ip+":"+str(Port))

    def run(self):
        Name_of_file = 'demo.txt'
        f = open(Name_of_file, 'rb')
        while True:
            l = f.read(BUFFER_SIZE)
            while (l):
                self.socket.send(l)
                #print('Sent ',repr(l))
                l = f.read(BUFFER_SIZE)
            if not l:
                f.close()
                self.socket.close()
                break


tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
tcp_socket.bind((IP, PORT))
threads = []

while True:
    tcp_socket.listen(5)
    print("Incoming connections are being awaited...")
    (conn, (ip, port)) = tcp_socket.accept()
    print(' Received a connection from ', (ip, port))
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    threads.append(newthread)
        
for t in threads:
    t.join()