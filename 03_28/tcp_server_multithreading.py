from socket import *
from threading import Thread

serverPort = 12000

def handler(connectionSocket, n):
  while True:
    msg = connectionSocket.recv(1024)
    msg = msg.decode('utf-8')
        
    print(f'[Thread {n}] Recieved Message "{msg}"')

    if(msg == '.'):
      print('[*] Client closed the connection')
      break

    modifiedMsg = msg.upper()

    connectionSocket.send(modifiedMsg.encode('utf-8'))
  connectionSocket.close()

def main():
  serverSocket = socket(AF_INET, SOCK_STREAM)
  serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
  serverSocket.bind(('', serverPort))
  serverSocket.listen(1) 

  print(f'[+] Server listening on port {serverPort}')
  
  i=0
  while True:
    try:
      newSocket, clientAddress = serverSocket.accept()

      print(f'[+] Received Connection from: {clientAddress[0]}:{clientAddress[1]}')
      
      thread = Thread(target=handler, args=(newSocket, i))
      thread.start()
      i += 1
    except KeyboardInterrupt:
      print(f'\n[!] Server Closed')
      break;

if __name__ == '__main__':
  main()
