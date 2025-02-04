import socket
import time 

serverName = 'localhost'
serverPort = 12000
address = (serverName, serverPort)

print("Creating UDP Server socket...")

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSocket.bind(address)

# while loop is used here because the server is always listening 
while True: 
    data, addr = serverSocket.recvfrom(4096)

    print(f"Server received data. Data: {data.decode()}, Address: {addr}")
    
    # NOTE: time delay does not affect anything 
    # time.sleep(10)

    serverSocket.sendto(data, addr)
