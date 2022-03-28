from socket import socket, AF_INET, SOCK_STREAM
import sys

serverName = 'localhost'
serverPort = 12000

def main():
  clientSocket = socket(AF_INET, SOCK_STREAM)
  clientSocket.settimeout(2)
  try:
    clientSocket.connect((serverName, serverPort))
  except:
    print('[!] Timeout error')

  while True:
    #msg = input('Enter message: ')
    msg = sys.argv[1]
    clientSocket.send(msg.encode('utf-8'))
    
    if(msg == '.'):
        break

    modifiedMsg = clientSocket.recv(1024)
    print(f'From server: {modifiedMsg.decode("utf-8")}')
    
  clientSocket.close()

if __name__ == '__main__':
    main()
