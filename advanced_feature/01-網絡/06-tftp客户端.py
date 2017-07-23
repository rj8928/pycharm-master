#coding=utf-8
from socket import *
import struct
import sys


udp_socket = socket(AF_INET,SOCK_DGRAM)

file_name = "tftp1.png"
send_head = struct.pack("!H%dsb5sb"%(len(file_name)),1,file_name,0,"octet",0)
udp_socket.sendto(send_head,("192.168.198.1", 69))

recv_data,recv_port = udp_socket.recvfrom(1024)
num,cu_block_num =struct.unpack("!HH",recv_data[:4])
print(recv_port[1])
fw = open(file_name,"a")
block_num = 0
recv_data_len = len(recv_data)
while True:
    if num ==3:
        if block_num+1 == cu_block_num:
            fw.write(recv_data[4:])
            block_num +=1
            send_ack =struct.pack("!HH",4,cu_block_num)
            udp_socket.sendto(send_ack,("192.168.198.1",recv_port[1]))

        recv_data,recv_port = udp_socket.recvfrom(1024)
        num,cu_block_num =struct.unpack("!HH",recv_data[:4])
        recv_data_len = len(recv_data)

        if recv_data_len < 516:
            print("over")
            break
        if num == 5:
            print("error")
            break



fw.close()
    

#udp_socket.sendto()
udp_socket.close()
