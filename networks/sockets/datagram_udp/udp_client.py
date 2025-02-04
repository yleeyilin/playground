import socket

clientName = 'localhost'
clientPort = 12000
address = (clientName, clientPort)

print("Creating UDP Client socket...")
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# wait for input
textInput = input("Write something: ")

# must ensure that serverSocket has been set up before this 
# line is triggered.
clientSocket.sendto(textInput.encode(), address)

# will wait until it hears from the socket 
data, addr = clientSocket.recvfrom(4096)

print(f"Client received data. Data: {data.decode()}, Address: {addr}")