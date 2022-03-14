from socket import socket, AF_INET, SOCK_DGRAM

def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM) 

    serverSocket.bind(('', serverPort))
    
    print(f'Server listening on port {serverPort}...')
    while True:
        msg, clientAddress = serverSocket.recvfrom(2048)
        print(f'Received connection form {clientAddress[0]}:{clientAddress[1]}')
        msg = msg.decode('utf-8')
        modifiedMsg = msg.upper()
        
        serverSocket.sendto(modifiedMsg.encode('utf-8'), clientAddress)



if __name__ == '__main__':
    main()
