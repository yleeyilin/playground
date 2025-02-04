import socket

# this is an example of a non-persistent tcp connection 

serverName = 'localhost'
serverPort = 12000

address = (serverName, serverPort)

# socket.socket() works too 
# default attr are socket.AF_INET, socket.SOCK_STREAM
serverWelcomeSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverWelcomeSocket.bind(address)
# set max length of the pending connections queue to 1 
serverWelcomeSocket.listen(1)

while True: 
    clientSocket, clientAddress = serverWelcomeSocket.accept()

    print(f"Client connected from {clientAddress}")

    # bc this is a streaming connection we use makefile instead of recv 
    input = clientSocket.makefile('r')

    input_text = [] # stores all the input in a array
    while (data := input.readline()): # when hvnt reach EOF
        input_text.append(data)
        print(repr(input_text))

    # TODO: FIGURE OUT WHY IT DOESNT REACH HERE
    print("REACHED HERE.")
    # sends all input text to the client socket 
    clientSocket.sendall(''.join(input_text).encode())

    # blocks both sending and receiving communication  
    clientSocket.shutdown(socket.SHUT_RDWR)

    # actually destroys the socket now 
    clientSocket.close()
    print("Closing connection.")