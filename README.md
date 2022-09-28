# Client-Server-communication-via-sockets
Client-Server communication via sockets, basic operations of a Web Server and Client and basic structures of HTTP messages
Requirements for execution:
• Python 3 version should be installed in the system to able to
execute the programs server.py and client.py
• No additional special package is required.
Note: The development of the programs was done on MAC OS.
Execution steps:
1. The first step is to open 2 different terminal and go into the
directory or folder “CN_ASSI” on all 2 terminals. if the folder is
placed on desktop.
cd desktop/CN_ASSI
2. Now on any two terminals execute the program file “server.py” to
invoke the servers in that specific order with any port number, for
example I’ve used 8080.
Terminal-1: python3 server.py 8080
Note: The server can handle multi process requests (multi-threading)
3. The next step is to execute the client program on the 2nd terminal
and web browser can be used, the following commands will allow
to execute.
Terminal-2: python3 client.py 127.0.0.1 8080 home.html
Web browser: http://localhost:8080/home.html
Note: for client terminal execution the format is as below.
Python3 client.py <host> <port> <filename with extension>
4. In the zip folder you can find another html file named:
home2.html.
Terminal-2: python3 client.py 127.0.0.1 8080 home2.html
Web browser: http://localhost:8080/home2.html
References:
1) https://docs.python.org/3/library/socketserver.html- code reference
TCP HTTP socket programming.
2) line 22-25 & line 48-65 reference link
https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/so
cket/addressing.html- used the link for retrieving address info.
