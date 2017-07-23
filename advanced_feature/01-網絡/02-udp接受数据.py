from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.bind(("",7788)) 
#def sendtext(text):
#    udpSocket.sendto(text,("192.168.198.1",8080))

#sendtext("hello")
recvData = udpSocket.recvfrom(1024)
content,destInfo = recvData

print(content.decode("gb2312"))
