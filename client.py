import socket

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((socket.gethostname(),6532))

message = client.recv(1024)

print(message)