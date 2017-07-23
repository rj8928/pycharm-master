from socket import *
from multiprocessing import Queue

def main():
    udp_socket = socket(AF_INET,SOCK_DGRAM)
    udp_socket.bind(("",7788))
    def rec_text(text):
        context,ipinfo = text
        print("从%s发送来一条消息:%s"%(ipinfo,context.decode("gb2312")))

    while True:
        text = udp_socket.recvfrom(1024)
        rec_text(text)

if __name__ == "__main__":
    main()
