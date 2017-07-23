from socket import *
from multiprocessing import Queue
from threading import Thread
import sys
def rec_text(text):
    context,ipinfo = text
    print("从%s发送来一条消息:%s"%(ipinfo,context.decode("gb2312")))

def send_text(IPINFO,Port):
    while True:
        Text = input("请输入要发送的消息:")
       # if Text == "quit":
       #     exit()
        udp_socket.sendto(Text.encode("gb2312"),(IPINFO,Port))
        print("发送成功")
udp_socket = None
def main():
    global udp_socket
    text = None
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(("",7788))

    IPINFO = input("请输入对方的ip地址:")
    Port = int(input("请输入对方的端口号:"))
    #Text = input("请输入要发送的消息:")

    send = Thread(target = send_text,args=(IPINFO,Port))
    send.start()
    while True:
        text = udp_socket.recvfrom(1024)
        recv = Thread(target = rec_text,args=(text,))
        recv.start()
            

if __name__ == "__main__":
    main()
