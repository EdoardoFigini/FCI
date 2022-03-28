from socket import socket, AF_INET, SOCK_STREAM
import sys

serverName = 'localhost'
serverPort = 12000

def main():
  clientSocket = socket(AF_INET, SOCK_STREAM)
  clientSocket.connect((serverName, serverPort))
    
  msg = sys.argv[1]
  clientSocket.send(msg.encode('utf-8'))

  modifiedMsg = clientSocket.recv(1024)
  print(f'From server: {modifiedMsg.decode("utf-8")}')

  clientSocket.close()

if __name__ == '__main__':
    main()
