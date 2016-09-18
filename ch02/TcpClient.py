from socket import *

HOST = 'localhost'
PORT = 21567
BUFSIZ = 1024



host = input('>host:\t')
port = int(input('>port:\t'))
if not host:
    host = HOST
if not port:
    port = PORT

address = (host, port)
tcpCliSock = socket(AF_INET, SOCK_STREAM)
tcpCliSock.connect(address)

while True:
    data = input('> ')
    if not data:
        break
    tcpCliSock.send(data.encode())
    data = tcpCliSock.recv(BUFSIZ)
    if not data:
        break
    print(data.decode())

tcpCliSock.close()