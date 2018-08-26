from socket import *
serverName = 'localhost'
serverPort = 13000
clientSocket = socket(AF_INET, SOCK_DGRAM)
while 1:
  message = input('Input two number and expression with space: ')
  if message == 'close':
    break
  byt = message.encode()
  clientSocket.sendto(byt, (serverName, serverPort))
  result, serverAddress = clientSocket.recvfrom(2048)
  print('Result :' + result.decode())
clientSocket.close()
