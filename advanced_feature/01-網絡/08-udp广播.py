#coding=utf-8
import socket,sys

dest = ("<broadcast>",7788)
#udp套接字
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
#需要广播加下一句
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

s.sendto("hi",dest)

print("等待回复")

while True:
    buf,addresss.recvfrom(2048)
    print("%s:%s"%(addresss,buf))
