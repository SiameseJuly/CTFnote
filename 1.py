import SocketServer 
from time import ctime



HOST = ''

PORT = 21567

ADDR = (HOST,PORT)



########################################################################
class MyRequestHandler(SocketServer.StreamRequestHandler):
    """"""

    #----------------------------------------------------------------------
    def handle(self):
        """Constructor"""
        print '.....connected from:', self.client_address
        self.wfile.write('[%s] %s' % (ctime(),self.rfile.readline()))
        

tcpServ = SocketServer.TCPServer(ADDR, MyRequestHandler)

print 'waiting for connection....'
tcpServ.serve_forever()
        
        
    
    