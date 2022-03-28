from socket import socket, AF_INET, SOCK_STREAM

serverPort = 12000

def main():
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.bind(('', serverPort))
  serverSocket.listen(1) #WELCOMESOCKET (argomento -> coda)

  print(f'[+] Server listening on port {serverPort}')

  while 1:
    try:
      connectionSocket, clientAddress = serverSocket.accept()

      print(f'[+] Received Connection from: {clientAddress[0]}:{clientAddress[1]}')

      msg = connectionSocket.recv(1024)
      msg = msg.decode('utf-8')

      modifiedMsg = msg.upper()

      connectionSocket.send(modifiedMsg.encode('utf-8'))
      connectionSocket.close()
    
    except KeyboardInterrupt:
      print(f'\n[!] Server Closed')
      break;

if __name__ == '__main__':
  main()
