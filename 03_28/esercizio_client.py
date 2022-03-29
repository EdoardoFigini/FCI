from socket import socket, AF_INET, SOCK_STREAM
from time import sleep

serverName = 'localhost'
serverPort = 12000

def main():
  clientSocket = socket(AF_INET, SOCK_STREAM)
  clientSocket.connect((serverName, serverPort))
  
  for i in range(100):
    msg = 'c'
    clientSocket.send(msg.encode('utf-8'))
    sleep(1)

  clientSocket.send('.'.encode('utf-8'))
  clientSocket.close()


if __name__ == '__main__':
    main()
