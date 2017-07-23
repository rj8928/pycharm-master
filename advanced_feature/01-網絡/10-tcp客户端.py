from socket import *
import time
clientSocket = socket(AF_INET,SOCK_STREAM)
clientSocket.connect(("192.168.198.130",7788))

clientSocket.send("haha".encode("utf-8"))

recv_data = clientSocket.recv(1024)
time.sleep(10)
print(recv_data)

clientSocket.close()
