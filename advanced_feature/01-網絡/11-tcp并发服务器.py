from socket import *
from threading import Thread
from time import sleep
def deal_new_socket(new_socket,Info):
    while True:
        recv_data = new_socket.recv(1024)
        if len(recv_data)>0:
            print("%s:%s"%(Info,recv_data))
        else:
            print("客户端关闭")
            break
    new_socket.close()

def main():
    tcp_socket = socket(AF_INET,SOCK_STREAM)
    tcp_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    tcp_socket.bind(("",7788))
    tcp_socket.listen(5)
    while True:
        new_socket,Info = tcp_socket.accept()
        t1 = Thread(target=deal_new_socket,args=(new_socket,Info))
        t1.start()
        #new_socket.close()
    tcp_socket.close()







if __name__ == "__main__":
    main()
