
# This is to create a separate process or thread to handle each request
from socketserver import ThreadingMixIn 
from http.server import BaseHTTPRequestHandler, HTTPServer
#The sys module provides information about constants, functions and methods of the Python interpreter.
import sys
import os
import glob #import glob. # Returns a list of names in list files


# Name_of_file values if host ip, port number and file name
HOST_IP = "127.0.0.1"
PORT_NUMBER = 9001
Name_of_file = "./index.html"


# this class handles the request send by client
class HandleRequest(BaseHTTPRequestHandler):
    def do_GET(own):
        print("\n*****Connected to the client*******\n")
        print("IP Address of the Client: " + own.address_string())
        print("Port Number of Client: " + str(own.client_address[1]))
        print("Socket Type: " + str(own.connection.type))
        print("Socket Family: " + str(own.connection.family))
        print("Socket Protocol: " + str(own.connection.proto))
        print("Peer Name: " + str(own.connection.getpeername()))
        print("Socket Address: " + str(own.connection.getsockname()))
        

        path_file = check_file(own.path)

# whether the file exists in the directory
        if path_file is not None:
            own.send_response(200)
            own.end_headers()

            with open(path_file, 'rb') as upload:
                file = upload.read()
                own.wfile.write(file)
            print("\n***Done with the process***\n")

# if there isn't a file in the directory
        else:
            own.send_response(404)
            own.end_headers()
        return

#This class manages the threads for the httpserver
class MultiThreadedHTTP(ThreadingMixIn, HTTPServer):
    """
     
    """


# function that verifies the port number's authenticity
def check_port(portnumber):
    try:
        PORT_NUMBER = int(portnumber)
    except:
        print("Using port number 9001 by Name_of_file. Provided port number cannot be accepted.")
    return portnumber


# function for determining the correctness of a file name's path
def check_file(Name_of_file):
    if Name_of_file == '/':
        return Name_of_file
    # whether the file's path is correct
    else:
        get = glob.glob("." + Name_of_file)
        if not get:  #path is invalid
            return None
        else:
            for location in get:
                if os.path.isfile(location):
                    return location  # a path has been discovered
            return None

# Main function
def main():
    global PORT_NUMBER
    #sys.argv is the list of commandline arguments passed to the Python program.
    if len(sys.argv) <= 1:
        print("No port number provided. Name_of_file value 9001 is used.")
    else:
        portnumber = int(sys.argv[1])
        PORT_NUMBER = check_port(portnumber)

    try:
        name_of_server = MultiThreadedHTTP((HOST_IP, PORT_NUMBER), HandleRequest)
        print("Server has been started, waiting for conections:\n")
        name_of_server.serve_forever()
    except:
        name_of_server.server_close()  # close the server


if __name__ == '__main__':
    main()
