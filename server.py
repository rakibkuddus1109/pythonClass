import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.bind((socket.gethostname(),6532))   # Setting up server

client.listen(5)   # No. of accepted connections

while True:
    sc1,ip_addr = client.accept()
    print("{} connected successfully".format(ip_addr))
    sc1.send(bytes('Connected Successfully!','utf-8'))
    sc1.close()


# socket() -- used for creating a socket object..
# bind() -- used to associate the socket with a specific ip address and port number..
# listen() -- it will listen for the connections from the clients.
# accept() -- to accept the connection..
# connect() -- client call connect to establish connection with server..
# send() -- for sending the messages..
# recv() -- for receiving the messages which client got from the server.
# close() -- for closing the connection which is established..
