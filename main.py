from socket import *
serverPort = 8080
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('127.0.0.1', serverPort))
serverSocket.listen(1)
while True:
    connectionSocket, addr = serverSocket.accept()
    print("THUMBS UP 👍")
    try:
        message = connectionSocket.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        outputdata = f.read()
        m='\nHTTP/1.1 200 OK\n\n'
        connectionSocket.send(m.encode("utf-8"))
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode("utf-8"))
        connectionSocket.close()
    except IOError:
        o='\nHTTP/1.1 404 Not Found\n\n'
        connectionSocket.send(o.encode("utf-8"))
        connectionSocket.close()

