from socket import socket, AF_INET, SOCK_DGRAM
import sys


def main():
    serverName = 'localhost' #'127.0.0.1'
    serverPort = 12000
    
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    
    msg = sys.argv[1]

    clientSocket.sendto(msg.encode('utf-8'), (serverName, serverPort))

    modifiedMsg, serverAddress = clientSocket.recvfrom(1024)
    
    print(modifiedMsg.decode('utf-8'))

if __name__ == '__main__':
    main()
