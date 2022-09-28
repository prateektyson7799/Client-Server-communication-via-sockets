###################################################################################################
# Author :  Nama Sai Krishna Prateek
# UTA ID : 1001880903
# Description : This program will initaite a request to the server which is given in command line along with the file
# requesting and the server will return contents of the file if found. The program will so display family,socktype,protocol,
# timeout and peer name.
#
# Citations : 1)1)https://docs.python.org/3/library/socketserver.html- code reference TCP HTTP socket programming
#             2)line 22-25 & line 48-65 reference link - https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/socket/addressing.html-
#               used the link for retrieving address info
#
####################################################################################################

import socket
import sys
import time
HOST, PORT = sys.argv[1],int(sys.argv[2])
data = sys.argv[3]

flag = False
""" Code obtained from https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/socket/addressing.html for fetching get address """
#start of reference code
def get_constants(prefix):

    #mapping constants to their names.
    return dict( (getattr(socket, n), n)
                 for n in dir(socket)
                 if n.startswith(prefix))


    #end of reference code

# Create a socket (SOCK_STREAM means a TCP socket)
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    # Connect to server and send data
    print("Connecting to server..........:", HOST, PORT)
    try:
        sock.connect((HOST, PORT)) #connecting to server
        send_time = time.time() #calculating send time
        flag = True
    except:
        print("Check server address")
    if flag == False:
        exit()
    print("Sent:     {}".format(data))
    sock.sendall(bytes(data + "\n", "utf-8")) #requesting file from server

    # Receive data from the server and shut down
    received = str(sock.recv(1024),"utf-8")
receive_time = time.time() #calculating receiving time
""" Code obtained from https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/socket/addressing.html for fetching get address """
#start of reference code
families = get_constants('AF_') #assigning prefix for creation of dictionary
types = get_constants('SOCK_')#assigning prefix for creation of dictionary
protocols = get_constants('IPPROTO_')#assigning prefix for creation of dictionary

for response in socket.getaddrinfo(HOST, PORT,
                                   socket.AF_INET,      # family
                                   socket.SOCK_STREAM,  # socktype
                                   socket.IPPROTO_TCP,  # protocol
                                   socket.AI_CANONNAME, # flags
                                   ):

    # Unpack the response tuple
    family, socktype, proto, canonname, sockaddr = response

    print('Family        :', families[family]) #display fmaily
    print('Type          :', types[socktype]) #display type
    print('Protocol      :', protocols[proto]) #display protocol
    print('Peer name:', sockaddr) #display peer name
    #end of reference code
print("Timeout:",sock.gettimeout()) #display timeout


RTT = receive_time - send_time #calculating round trip time
print("Status: {}".format(received[0:16])) #display the status
if "404" in received[0:16]:
    print("File not FOUND")
    exit()
print("Received file content: {}".format(received[17:])) #display contents of the receiving file
print("RTT:",RTT)# display RTT
