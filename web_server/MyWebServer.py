#coding:utf-8
from socket import *
from multiprocessing import Process
import re
import sys


#设置静态文件根目录
HTML_ROOT_DIR = "./html"
PY_TEST_ROOT_DIR = "./test_py"


class HTTPServer(object):

    def __init__(self,application):
        """构造函数，application指的是框架的app"""
        self.tcp_socket = socket(AF_INET, SOCK_STREAM)
        self.tcp_socket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
        self.app = application
        #self.tcp_socket.bind(("", port))
        # tcp_socket.listen(128)
    def bind(self,port):
        self.tcp_socket.bind(("",port))

    def start(self):
        self.tcp_socket.listen(128)
        while True:
            cli_socket, cli_address = self.tcp_socket.accept()
            print ("%s已连接"%str(cli_address))
            p = Process(target=self.fun, args=(cli_socket,))
            p.start()
            cli_socket.close()


    def start_response(self, status, headers):
        # server_headers =[
        #     ("Server","MY Server")
        # ]
        response_headers = "HTTP/1.1" + status + "\r\n"
        for header in headers:
            response_headers +="%s: %s\r\n"%header
        self.response_headers = response_headers



    def fun(self,cli_socket):
        # 接收数据
        # 获取客户端请求数据
        request_data = cli_socket.recv(1024)
        request_line = request_data.splitlines()
        for line in request_line:
            print(line)
         # 'GET / HTTP/1.1'
        start_line = request_line[0]
        # 提取用户请求的文件
        file_name = re.match(r"\w+ +(/[^ ]*) ",start_line.decode("utf-8")).group(1)
        method = re.match(r"(\w+) +/[^ ]* ",start_line.decode("utf-8")).group(1)
        env = {
            "PATH_INFO": file_name,
            "METHOD": method
        }
        response_body = self.app(env,self.start_response)
        response = self.response_headers + "\r\n" + response_body

        # 向客户的返回响应数据
        cli_socket.send(bytes(response, "utf-8"))
        #关闭客户端连接
        cli_socket.close()


def main():
    sys.path.insert(1,PY_TEST_ROOT_DIR)
    if len(sys.argv)<2:
        sys.exit("Python MyWebServer.py Module:app")
    module_name, app_name = sys.argv[1].split(":")
    m = __import__(module_name)
    app = getattr(m,app_name)
    #app = Application()
    http_server = HTTPServer(app)
    http_server.bind(8000)
    http_server.start()

if __name__ == '__main__':
    main()
