from socket import socket, AF_INET, SOCK_DGRAM

def main():
    serverPort = 12000
    serverSocket = socket(AF_INET, SOCK_DGRAM) 

    serverSocket.bind(('', serverPort))
    
    vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}

    print(f'Server listening on port {serverPort}...')
    while True:
        msg, clientAddress = serverSocket.recvfrom(2048)
        print(f'Received connection form {clientAddress[0]}:{clientAddress[1]}')
        msg = msg.decode('utf-8')
        
        count = 0
        for c in msg:
            if c not in vowels:
                count += 1
        
        serverSocket.sendto(str(count).encode('utf-8'), clientAddress)



if __name__ == '__main__':
    main()
