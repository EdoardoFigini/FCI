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
        
        if (int(msg) <= 2):
            return

        primo=True
        for i in range(2, int(msg)):
            if(int(msg)%i==0):
                primo = False
                break

        serverSocket.sendto(['Il numero non è primo', 'Il numero è primo'][primo].encode('utf-8'), clientAddress)



if __name__ == '__main__':
    main()
