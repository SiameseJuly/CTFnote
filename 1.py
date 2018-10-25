import SocketServer 
from time import ctime

HOST = ''

PORT = 21567

ADDR = (HOST,PORT)



class MyRequestHandler(SocketServer.StreamRequestHandler):
    """"""

    #----------------------------------------------------------------------
    def handle(self):
        """Constructor"""
        print '.....connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(),self.rfile.readline()))

        self.request.send("""hello,welcome to halfbit
        This is Crypto test ,please help me do test """                     
        )
        self.request.send(b'\nls\n')

    
        while True:
            self.request.send(b"\n's'um or 't'imes or 'p'rint\n")
            c = self.request.recv(1024)[:-1]
            print c
        if c == '1':
            self.request.send(b'5 + 4 = ?\n')
            c = self.request.recv(1024)[:-1]
            if c == b'9':
                self.request.send("ctf{sum}\n")
            else:
                self.request.send("wrong!\n")
                
        elif c == b'2':
            self.request.send(b'3 * 2 = ?\n')
            c = self.request.recv(1024)[:-1]  
            if c == b'6':
                self.request.send("ctf{times}\n")
            else:
                self.request.send("wrong!\n")            
        elif c == b'3':
            self.request.send("ctf{print}")
        self.request.close()        
        

tcpServ = SocketServer.TCPServer(ADDR, MyRequestHandler)
tcpServ.allow_reuse_address = True
print 'waiting for connection....'
tcpServ.serve_forever()
        
        
    
    
