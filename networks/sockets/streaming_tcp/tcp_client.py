import socket

# tcp 3-way handshake is at the transport layer
# this means that the applications / processes are not aware 

clientName = 'localhost'
clientPort = 12000

address = (clientName, clientPort)

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
clientSocket.connect(address) # initiates a 3 way handshake 

while text := input(): # bc this is a streaming request
    clientSocket.send(text.encode())
    clientSocket.send(b'\r\n')

clientSocket.sendall(b'\r\n') # flush all 

while data := clientSocket.recv(10): 
    print(repr(data)) # or print(data.decode())

clientSocket.close()