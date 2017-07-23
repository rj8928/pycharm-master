from socket import *

serverSocket = socket(AF_INET,SOCK_STREAM)#创建tcp套接字

serverSocket.bind(("",8989))#端口绑定

serverSocket.listen(5)#最大客户端数

clientSocket,clientInfo = serverSocket.accept()#接受客户端信息

recv_data = clientSocket.recv(1024)#接受客户端数据

print("%s:%s"%(str(clientInfo),recv_data))

clientSocket.close()
serverSocket.close()
