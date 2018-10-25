
import socketserver

import time

class MyRequestHandler(SocketServer.StreamRequestHandler):  #StreamRequestHandler实现TCP/UDP服务器的服务处理器
    def handle(self):  #重写接收响应函数
        print('...connect from:', self.client_address)
        data = self.rfile.readline().strip()
        print(data)
        self.wfile.write('[%s] %s' % (ctime(), data))




if __name__ == "__main__":
    HOST, PORT = '118.24.130.180', 10086
    server = ThreadedServer((HOST, PORT), process)
    server.allow_reuse_address = True
    server.serve_forever()