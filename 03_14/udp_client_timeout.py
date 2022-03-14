from socket import socket, AF_INET, SOCK_DGRAM, timeout
import sys


def main():
    serverName = 'localhost' #'127.0.0.1'
    serverPort = 12000
    
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.settimeout(1)

    msg = sys.argv[1]

    clientSocket.sendto(msg.encode('utf-8'), (serverName, serverPort))
    
    try:
        modifiedMsg, serverAddress = clientSocket.recvfrom(1024)
    
        print(modifiedMsg.decode('utf-8'))
    
    except timeout as e:
        print(f'Error: {e}')
        sys.exit(1)
        
    finally:
        clientSocket.close()

if __name__ == '__main__':
    main()
