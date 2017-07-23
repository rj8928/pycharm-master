#coding:utf-8
from socket import *
from multiprocessing import Process
import re

#设置静态文件根目录
HTML_ROOT_DIR = "."

def fun(cli_socket):
    # 接收数据
    # 获取客户端请求数据
    request_data = cli_socket.recv(1024)
    # print (request_data)
    request_line = request_data.splitlines()
    for line in request_line:
        print(line)
     # 'GET / HTTP/1.1'
    start_line = request_line[0]
    print("*"*50)
    print(start_line)
    # 提取用户请求的文件
    file_name = re.match(r"\w+ +(/[^ ]*) ",start_line.decode("utf-8")).group(1)
    print("*"*50)
    print(file_name)

    if "/" == file_name:
        file_name = "/index.html"
    # file_name = HTML_ROOT_DIR+file_name    ###for test
    # print(file_name)
    # 打开文件，读取内容
    try:
        request_file = open (HTML_ROOT_DIR + file_name,"rb")
    except IOError:
        response_start = "HTTP/1.1 404 Not Found\r\n"
        response_headers = "Server: my server\r\n"
        response_body = "The file is not found! 555"
    else:
        file_data = request_file.read()
        request_file.close()
    # 构造响应数据
        response_start = "HTTP/1.1 200 OK\r\n"
        response_headers = "Server: My server\r\n"
        response_body = file_data.decode("utf-8")
    response = response_start + response_headers + "\r\n" + response_body
    #print (response)
    # 向客户的返回响应数据
    cli_socket.send(bytes(response,"utf-8"))
    #关闭客户端连接
    cli_socket.close()

    # 解析http报文数据 request_data
    # 提取请求方式
    # 提取请求响应路径
    # 返回响应数据
    #tcp socket 服务端

def main():
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

    tcp_socket.bind(("", 8000))
    tcp_socket.listen(128)
    while True:
        cli_socket, cli_address = tcp_socket.accept()
        print ("%s已连接"%str(cli_address))
        p = Process(target=fun, args=(cli_socket,))
        p.start()
        cli_socket.close()


if __name__ == '__main__':
    main()
