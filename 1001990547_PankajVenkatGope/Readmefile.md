## Name: Pankaj Venkat Gope
## UTA ID: 1001990547
## Email ID: pvg0547@mavs.uta.edu
## Contact Number: +16825515087


*****************************************************************************************************************************************
## Description
I've created a multi-threaded Web server that communicates with any standard Web Clients and tested the functionality with a web browser.HTTP is a text-based protocol that connects the Web server and the Web client (Hypertext Transfer Protocol) 
Created my own single-threaded Web Client that communicates with my Web Server and downloads a file from it. 
Shows the most important connection parameters for both the Web client (on the server side) and the Web server (on the client side).

*****************************************************************************************************************************************

## Description of the code
1. Server is expected to function exclusively with HTTP get messages and is multi-threaded to handle several requests at the same time. 
2. When starting the application, the port number can be specified as an argument; otherwise, the default port number of 9001 is used. 
3. Incoming client requests can be handled by the server, which can also show important client information. 
4. If no file is requested, the server responds with the default file. If the client requests a file that is not available on the server, the server responds with "HTTP/1.1 404 Not Found." 
5. If the server has the file the client requested, it responds with "HTTP/1.1 200 OK." 
6. Client establishes a connection with the server and sends a file request.
7. Client establishes a connection with the server and sends a file request. 
8. The client also shows important server information.


## How to run the code:

Step 1 : The following interpretor is used to implement the code: 

"Python 3.9"

*****************************************************************************************************************************************

Step 2 :
Running my_server.py:

my_server.py port_number

example : python3 my_server.py 9001

output: Server has been started, waiting for conections:


Note: The port number is purely optional. If no value is specified, the default value of 9001 is utilized.

*****************************************************************************************************************************************

Step 3 :

Running my_client.py:

my_client.py host_name port_number file_name

example : python3 my_client.py 127.0.0.1 9001 pankaj.txt

Output:
   
   The response has been Received

Server: BaseHTTP/0.6 Python/3.9.10
Date: Fri, 18 Mar 2022 21:28:36 GMT


HTTP/1.0
200 OK

Hello My name is Pankaj Gope

Round Trip Time (RTT): 0.002003908157348633
Server Port Number: 9001
Host IP: 127.0.0.1
Family of the socket: AddressFamily.AF_INET
Socket Tyop: SocketKind.SOCK_STREAM
Socket Protocol: 6
Peer Name: ('127.0.0.1', 9001)

     Done


Note: Optional fields include host name, port number, and file name. If no value is specified, the default settings of "127.0.0.1", "9001", and "demo.html" are utilized. The sequence in which the arguments are presented is important.

*****************************************************************************************************************************************

*****After the client is connected to the server, it shows the following output:*****

Connected to the client

IP Address of the Client: 127.0.0.1
Port Number of Client: 65461
Socket Type: SocketKind.SOCK_STREAM
Socket Family: AddressFamily.AF_INET
Socket Protocol: 0
Peer Name: ('127.0.0.1', 65461)
Socket Address: ('127.0.0.1', 9001)
127.0.0.1 - - [18/Mar/2022 16:28:36] "GET /pankaj.txt HTTP/1.1" 200 -

Done with the process


and it waits for another clients request.
multiple clients can be connected at the same time to the server and get the expected result.

*****************************************************************************************************************************************

Step 4 :

Running it on the local host

http://localhost:9001/pankaj.txt
or
http://localhost:9001/demo.html
or
http://localhost:9001/Readmefile.md

or any other file(txt,html) that will be made inside the folder.

*****************************************************************************************************************************************

-> References
https://documentation.help/Python-2.7.13/basehttpserver.html
https://python.readthedocs.io/en/v2.7.2/library/basehttpserver.html
https://docs.python.org/3/library/http.server.html
https://stackoverflow.com/questions/1557571/how-do-i-get-time-of-a-python-programs-execution
https://www.programcreek.com/python/example/103649/http.server.BaseHTTPRequestHandler
https://pythonbasics.org/webserver/
https://www.geeksforgeeks.org/socket-programming-python/