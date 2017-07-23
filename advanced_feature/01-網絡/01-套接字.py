from socket import *
udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.bind(("",7788)) 
def sendtext(text):
    udpSocket.sendto(text.encode("utf-8"),("192.168.198.1",8080))

text = input("请输入要发送的消息:")
sendtext(text)
