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
        msg = connectionSocket.recv(1024).decode('utf-8')
        print(f' \u221F  Recieved {len(msg)} messages')

        if(msg == '.'):
          break

      connectionSocket.close()
        
      print('[*] Client closed the connection')
    except KeyboardInterrupt:
      print(f'\n[!] Server Closed')
      break;

if __name__ == '__main__':
  main()
