from socket import *
serverPort = 13000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('Server is ready to receive: ')
while 1:
  message, clientAddress = serverSocket.recvfrom(2048, )
  array = message.decode().split()
  result = 0
  if array[1] == '+':
    result = int(array[0]) + int(array[2])
  if array[1] == '-':
    result = int(array[0]) - int(array[2])
  if array[1] == '*':
    result = int(array[0]) * int(array[2])
  if array[1] == '/':
    result = int(array[0]) / int(array[2])
  result = str(result)
  print('\nExpressing: ' + str(message.decode()) +'\nSent result: ' + result + ' to '+ str(clientAddress))
  result = result.encode()
  serverSocket.sendto(result, clientAddress)

