###########################################################################################################################################
# Author :  Nama Sai Krishna Prateek
# UTA ID : 1001880903
# Description : This program will invoke server on localhost with port 8080 as default or to any given port in command line as argument.
# The server waits indefinitely till a request comes. it will check the requested file and searched it's dictionary and sends the content
# of the file. The server can also handle multiple requests (multi-threading). it also displays family,socktype,protocol,
# timeout and peer name.
# Citations : 1)https://docs.python.org/3/library/socketserver.html- code reference TCP HTTP socket programming
#             2)line 22-25 & line 48-65 reference link - https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/socket/addressing.html-
#               used the link for retrieving address info
#
#
#############################################################################################################################################

import socketserver
from os import path
import os
import sys
import socket
path = os.path.abspath(os.getcwd()) #code for getting the local path
u_file = "HTTP/1.0 404 BAD\r\n"+"Content-Type: text/html\r\n\r\n"+"<HTML><TITLE>404 NOT FOUND</TITLE><H1>404 NOT FOUND</H1><BODY>UNABLE TO FIND FILE</BODY></HTML>"
#local varaible contenting bad file or not found text
class MyTCPHandler(socketserver.StreamRequestHandler):

    """ Code obtained from https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/socket/addressing.html for fetching get address """
    #start of reference code
    def get_constants(self,prefix):
        #mapping constants to their names.
        return dict( (getattr(socket, n), n)
                     for n in dir(socket)
                     if n.startswith(prefix))

    #end of reference code
    def getContent(self, path,file): #Get contents of the requested files and adding HTTP header
        path_lv = path + "/" + file
        try:
            with open(path_lv, mode='r', encoding='utf-8') as f: #file opening
                content = f.read()
            f.close()
            content = "HTTP/1.0 200 OK\r\n"+"Content-Type: text/html\r\n\r\n"+ content #adding HTTP header
        except IOError:
            print("unable to open files") #display if unable to open f sile
        print("File sent.")
        return bytes(content, 'utf-8') #returning content of file

    def handle(self):

        self.data = self.rfile.readline().strip() #receiving info of request
        print("client: {} requesting:".format(self.client_address[0])) #printing out requsting client address
        files = os.listdir() #fetching local Directory files names
        req_file = str(self.data).split("'") #filtering requested data
        print(str(req_file[1]))#display the requested data

        #start of reference code
        families = self.get_constants('AF_') #assigning prefix for creation of dictionary
        types = self.get_constants('SOCK_')#assigning prefix for creation of dictionary
        protocols = self.get_constants('IPPROTO_')#assigning prefix for creation of dictionary
        """ Code obtained from https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/socket/addressing.html for fetching get address """

        for response in socket.getaddrinfo(HOST, PORT,
                                           socket.AF_INET,      # family
                                           socket.SOCK_STREAM,  # socktype
                                           socket.IPPROTO_TCP,  # protocol
                                           socket.AI_CANONNAME, # flags
                                           ):

            # Unpack the response tuple
            family, socktype, proto, canonname, sockaddr = response

            print('Family        :', families[family])
            print('Type          :', types[socktype])
            print('Protocol      :', protocols[proto])
        #end of reference code
            print('Peer name:', sockaddr[0])

        if str(req_file[1]) in files: #check if file is in dictionary
            print("Sending file.")
            self.wfile.write(bytes(self.getContent(path,str(req_file[1])))) #send the contents the requester
            return
        elif "GET" in str(req_file[1]): #check if GET command
            lv = str(req_file[1]).split("/") #filtering the string
            lv_s = str(lv[1]).split(" ") #filtering the string
            if str(lv_s[0]) in files: #check if file is in dictionary
                print("Sending file.")
                self.wfile.write(bytes(self.getContent(path,str(lv_s[0])))) #send the contents the requester
            else:
                print("File not Found.")
                self.wfile.write(bytes(u_file, 'utf-8')) #file not found
        else:
            print("File not Found.")
            self.wfile.write(bytes(u_file, 'utf-8')) #file not found

if __name__ == "__main__":
    if len(sys.argv) > 1:
        HOST, PORT = "localhost", int(sys.argv[1]) #assigning host and port
    else:
        HOST, PORT = "localhost", 8080

    print("Establishing server............")
    with socketserver.TCPServer((HOST, PORT), MyTCPHandler) as server: #calling socketserver and will handle multi-threading
        server.serve_forever() #making the server run continous
