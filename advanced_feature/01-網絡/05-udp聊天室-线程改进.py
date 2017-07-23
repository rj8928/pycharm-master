from threading import Thread
from socket import *
udp_scoket = None
    #1. 接受信息
def recv_data():
    while True:
        text = udp_scoket.recvfrom(1024)
        print("\r>>%s:%s"%(text[1],text[0].decode("gb2312")))
        print("<<",end="")
#2. 发送信息
def send_data(Ip_info,Port):
    while True:
        text = input("<<")
        udp_scoket.sendto(text.encode("gb2312"),(Ip_info,Port))

def main():
    global udp_scoket
    udp_scoket = socket(AF_INET,SOCK_DGRAM)
    recv = Thread(target=recv_data)
    recv.start()
    Ip_info = input("请输入对方ip:")
    Port = int(input("请输入对方端口:"))
    send = Thread(target=send_data,args=(Ip_info,Port))
    send.start()

    recv.join()
    send.join()


if __name__ == "__main__":
    main()
