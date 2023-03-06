
# importing modules
from time import *
import http.client
import time
import sys

# IP of the host, port number, and file name
HOST_IP = "127.0.0.1"
PORT_NUMBER = 9001
Name_of_file = "index.html"


# On HTTPServer, this class generates a client.
class HTTP():
    # a function that creates
    def __init__(own, ip_host, number_port, name_file):
        own.hostname = ip_host
        own.portnumber = number_port
        own.filename = name_file

    # a request-making function
    
    
    def request(own):
        connect = http.client.HTTPConnection(own.hostname + ':' + str(own.portnumber))

    # does a http request, transmits it, and prints the html file
        try:
            Time_of_Request = time.time()
            connect.request("GET", '/' + own.filename)
            Time_Recieved = time.time()
    # other crucial connection parameters are displayed
        except ConnectionRefusedError:
            print("The server was unable to establish a connection. It is Refused.\n")
            return

        # socket information and connection parameters
        family_socket = connect.sock.family
        protocol_socket = connect.sock.proto
        type_socket = connect.sock.type
        name_peer = connect.sock.getpeername()

        try:
            get = connect.getresponse()
        except:
            print("connection has been refused\n")
            return
        print("\n*****The response has been Received*****\n")

        # in the server, outputs the header details
        print(get.headers)
        # Check the http version and display the appropriate information.
        if get.version == 11:
            print("HTTP/1.1")
        # If the version is different, display the appropriate information.
        elif get.version == 10:
            print("HTTP/1.0")
        # Check the status of http and present the results as needed.
        if get.code == 200:
            print("200 OK\n")
        elif get.code == 404:
            print("404 NOT FOUND\n")
        
        # print the contents of the html file in the terminal
        print(get.read().decode('utf-8') + '\n')
        rtt = str(Time_Recieved - Time_of_Request)
        
        # On the server, print other connection parameters
        print("Round Trip Time (RTT): " + rtt)
        print("Server Port Number: " + str(connect.port))
        print("Host IP: " + connect.host)
        print("Family of the socket: " + str(family_socket))
        print("Socket Type: " + str(type_socket))
        print("Socket Protocol: " + str(protocol_socket))
        print("Peer Name: " + str(name_peer))
        print("\n*****Done*****\n")


def main():
    # Check the number of arguments that have been presented.
    
    if len(sys.argv) == 2:
        host_name = sys.argv[1]
        HOST_IP = host_name
        print("There is no port number specified. The default value of 9001 is utilized.")
        PORT_NUMBER = 9001
        print("There is no filename given. The filename is set to the default value.")
        Name_of_file = "index.html"

    # If no parameters are specified, default values will be used.
    elif len(sys.argv) == 3:
        host_name = sys.argv[1]
        port_number = sys.argv[2]
        HOST_IP = host_name
        PORT_NUMBER= port_number
        print("There is no filename given. The filename is set to the default value.")
        Name_of_file = "index.html"

    # If parameters are specified, display them.
    #sys. argv is a list in Python, which contains the command-line arguments passed to the script. 
    elif len(sys.argv) == 4:
        host_name = sys.argv[1]
        port_number = sys.argv[2]
        file_name = sys.argv[3]
        HOST_IP = host_name
        PORT_NUMBER= port_number
        Name_of_file = file_name
    else:
        print("No arguments provided. All default values are used.")
        HOST_IP = "127.0.0.1"
        PORT_NUMBER = 9001
        Name_of_file = "index.html"

    # Create a client and submit a request to it.
    user = HTTP(HOST_IP, PORT_NUMBER, Name_of_file)
    user.request()


if __name__ == "__main__":
    main()