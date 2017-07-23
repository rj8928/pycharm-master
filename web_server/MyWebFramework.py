import time
#from MyWebServer import HTTPServer
HTML_ROOT_DIR = "./html"
class Application(object):
    """框架的核心部分"""
    def __init__(self,urls):
        # 设置路由信息
        self.urls = urls

    def __call__(self, env, start_response):
        path = env.get("PATH_INFO","/")
        if path.startswith("/static"):
           file_name = path[7:]
           try:
                request_file = open (HTML_ROOT_DIR + file_name,"rb")
           except IOError:
                # 代表未找到路由信息，404错误
                status = "404 Not Found"
                headers = []
                start_response(status, headers)
                return "not found"
           else:
                file_data = request_file.read()
                request_file.close()
                    #构造响应数据
                status = "HTTP/1.1 200 OK\r\n"
                headers = []
                start_response(status, headers)
                return file_data.decode("utf-8")


        for url, handler in self.urls:
            if path == url:
                response_body = handler(env,start_response)
                return response_body

        # 代表未找到路由信息，404错误
        status = "404 Not Found"
        headers = []
        start_response(status, headers)
        return "not found"

def show_time(env, start_response):
    status = "200 OK"
    headers = [
        ("Context-Type", "text/plain")
    ]
    start_response(status, headers)
    return time.ctime()

def say_hello(env,start_response):
    status = "200 OK"
    headers = [
        ("Context-Type", "text/plain")
    ]
    start_response(status,headers)
    return "hello world"

urls = [
         ("/ctime", show_time),
         ("/sayhello",say_hello)
    ]
app = Application(urls)
# if __name__ == '__main__':
#
#     urls = [
#         ("/ctime", show_time),
#         ("/sayhello",say_hello)
#     ]
#
#     app = Application(urls)
#     http_server = HTTPServer(app)
#     http_server.bind(8000)
#     http_server.start()
