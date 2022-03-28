from socket import socket, AF_INET, SOCK_STREAM

serverPort = 12000

def main():
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.bind(('', serverPort))
  serverSocket.listen(1)

  print(f'[+] Server listening on port {serverPort}')

  while True:
    try:
      connectionSocket, clientAddress = serverSocket.accept()

      print(f'[+] Received Connection from: {clientAddress[0]}:{clientAddress[1]}')
      
      while True:
        msg = connectionSocket.recv(1024)
        msg = msg.decode('utf-8')
        
        print(f' |__ Recieved Message "{msg}"')

        if(msg == '.'):
          print('[*] Client closed the connection')
          break

        modifiedMsg = msg.upper()

        connectionSocket.send(modifiedMsg.encode('utf-8'))
      connectionSocket.close()
    
    except KeyboardInterrupt:
      print(f'\n[!] Server Closed')
      break;

if __name__ == '__main__':
  main()
