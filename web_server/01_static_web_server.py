#coding:utf-8
from socket import *
from multiprocessing import Process
from math import *

HTML_ROOT_DTR = ""


def fun(cli_socket):
    # 接收数据
    # 获取客户端请求数据
    request_data = cli_socket.recv(1024)
    print (request_data)
    # 构造响应数据
    response_start_line = "HTTP/1.1 200 OK\r\n"
    response_headers = "Server: My server\r\n"
    response_body = "hello world"
    response = response_start_line + response_headers + "\r\n" + response_body
    # print (response)
    # 向客户的返回响应数据
    cli_socket.send(bytes(response,"utf-8"))
    # 关闭客户端连接
    cli_socket.close()

    # 解析http报文数据 request_data
    # 提取请求方式
    # 提取请求响应路径
    # 返回响应数据
    # tcp socket 服务端

def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    tcp_socket.bind(("", 8000))
    tcp_socket.listen(10)
    while True:
        cli_socket, cli_address = tcp_socket.accept()
        print ("%s已连接"%str(cli_address))
        p = Process(target=fun, args=(cli_socket,))
        p.start()
        cli_socket.close()


if __name__ == '__main__':
    main()
