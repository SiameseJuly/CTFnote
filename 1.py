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

        self.request.send("hello,welcome to halfbit!\n")
        self.request.send("This is the world of Crypto.\n")
        self.request.send("Let's begin!\n")
        self.request.send("The challenge is init ...... please wait for a while.\n")
        level = 0
        goal = 0 
    
        while True:
            self.request.send("The challenge is begin!\n")
            self.request.send("Are you ready?\n")
            level = 0 if goal == 0 else goal
            

            if level == 0 :
                print "level = ",level
                print "goal = ",goal
                self.request.send("Level NO.0 the Simplest RSA\n!")
                self.request.send("if you get the d,give me halfbit{********}\n")
                self.request.send("p = 3487583947589437589237958723892346254777\n")
                self.request.send("q = 8767867843568934765983476584376578389\n")
                self.request.send("e = 65537\n")                
                result  = self.request.recv(1024)[:-1]
                
                if result == "halfbit{}" :
                    
                    goal = 1
                    self.request.send("Correct !\n")  
                    continue
                
                else:
                    self.request.send("Try again!!!!!\n")
                    continue
                
            elif level == 1 :
                print "level = ",level
                print "goal = ",goal
                self.request.send("Level NO.1 Violent Decomposition!\n")
                self.request.send("if you get the m,give me directly !\n")
                self.request.send("c = \n")
                self.request.send("N = 322831561921859\n")
                self.request.send("e = 23\n")    
                result  = self.request.recv(1024)[:-1]
                
                if result == "halfbit{}" :
                    goal = 2
                    self.request.send("Correct !\n")
                    continue
                
                else:   
                    self.request.send("Try again!!!!!\n")
                    continue
                
            elif level == 2 :
                print "level = ",level
                print "goal = ",goal
                self.request.send("Level NO.2 Modules Should Be Primes!\n")
                self.request.send("if you get the m,give me directly !Such as halfbit{********}\n")
                self.request.send("N1 = 9051013965404084482870087864821455535159008696042953021965631089095795348830954383127323853272528967729311045179605407693592665683311660581204886571146327720288455874927281128121117323579691204792399913106627543274457036172455814805715668293705603675386878220947722186914112990452722174363713630297685159669328951520891938403452797650685849523658191947411429068829734053745180460758604283051344339641429819373112365211739216160420494167071996438506850526168389386850499796102003625404245645796271690310748804327\n")
                self.request.send("N2 = 13225948396179603816062046418717214792668512413625091569997524364243995991961018894150059207824093837420451375240550310050209398964506318518991620142575926623780411532257230701985821629425722030608722035570690474171259238153947095310303522831971664666067542649034461621725656234869005501293423975184701929729170077280251436216167293058560030089006140224375425679571181787206982712477261432579537981278055755344573767076951793312062480275004564657590263719816033564139497109942073701755011873153205366238585665743\n")
                self.request.send("e = 23\n")                
                result  = self.request.recv(1024)[:-1]
                
                if result == "halfbit{}" :
                    goal = 3
                    self.request.send("Correct !\n")
                    continue
                
                else:   
                    self.request.send("Try again!!!!!\n")
                    continue
                
            elif level == 3 :
                print "level = ",level
                print "goal = ",goal
                self.request.send("Level NO.3 Common Modules Attack!\n")
                self.request.send("if you get the m,give me directly !Such as halfbit{********}\n")
                self.request.send(" \n")
                self.request.send("\n")
                self.request.send("\n")                
                self.request.send("ctf{print}")
                result  = self.request.recv(1024)[:-1]
                
                if result == "halfbit{}" :
                    goal = 4
                    self.request.send("Correct !\n")
                    continue
                
                else:   
                    self.request.send("Try again!!!!!\n")
                    continue
                
            elif level == 4 :
                print "level = ",level
                print "goal = ",goal
                self.request.send("Level NO.4 Small Plaintext Attack!\n")
                self.request.send("if you get the m,give me directly !Such as halfbit{********}\n")
                self.request.send(" \n")
                self.request.send("\n")
                self.request.send("\n")                
                self.request.send("ctf{print}")
                result  = self.request.recv(1024)[:-1]
                
                if result == "halfbit{}" :
                    goal = 5
                    self.request.send("Correct !\n")
                    continue
                
                else:   
                    self.request.send("Try again!!!!!\n")
                    continue 
                
            elif level == 5 :
                print "level = ",level
                print "goal = ",goal
                self.request.send("Level NO.5 Rabin!\n")
                self.request.send("if you get the m,give me directly !Such as halfbit{********}\n")
                self.request.send(" \n")
                self.request.send("\n")
                self.request.send("\n")                
                self.request.send("ctf{print}")
                result  = self.request.recv(1024)[:-1]
                
                if result == "halfbit{}" :
                    goal = 6
                    self.request.send("Correct !\n")
                    continue
                
                else:   
                    self.request.send("Try again!!!!!\n")
                    continue            

            elif level == 6 :
                print "level = ",level
                print "goal = ",goal
                self.request.send("Level NO.6 Broadcast attack!\n")
                self.request.send("if you get the m,give me directly !Such as halfbit{********}\n")
                self.request.send(" \n")
                self.request.send("\n")
                self.request.send("\n")                
                self.request.send("ctf{print}")
                result  = self.request.recv(1024)[:-1]
                
                if result == "halfbit{}" :
                    goal = 7
                    self.request.send("Correct !\n")
                    self.request.send("Congratulatios! You have finished the basical RSA lessons!!!!\n")
                    """
　　　ＢＢＢＢＢＢＢＢ　　　　　　　　ＢＢＢＢＢＢＢ　　　　　　　　　　　ＢＢ　　　　　　
　　　　　ＢＢ　ＢＢＢ　　　　　　　　ＢＢ　　　ＢＢ　　　　　　　　　　ＢＢＢ　　　　　　
　　　　　Ｂ　　　ＢＢＢ　　　　　　　ＢＢ　　　　Ｂ　　　　　　　　　　ＢＢＢ　　　　　　
　　　　　Ｂ　　　ＢＢ　　　　　　　　ＢＢＢＢ　　　　　　　　　　　　　Ｂ　ＢＢ　　　　　
　　　　　ＢＢＢＢＢＢ　　　　　　　　　ＢＢＢＢＢＢ　　　　　　　　　ＢＢ　ＢＢ　　　　　
　　　　　ＢＢ　ＢＢＢ　　　　　　　　　　　　ＢＢＢ　　　　　　　　　ＢＢＢＢＢＢ　　　　
　　　　　Ｂ　　　ＢＢ　　　　　　　　Ｂ　　　　ＢＢ　　　　　　　　ＢＢ　　　ＢＢ　　　　
　　　　　Ｂ　　　ＢＢＢ　　　　　　　ＢＢ　　　ＢＢ　　　　　　　　ＢＢ　　　ＢＢ　　　　
　　　ＢＢＢＢＢ　ＢＢＢ　　　　　　　ＢＢＢＢＢＢＢ　　　　　　　ＢＢＢ　　ＢＢＢＢＢ　　

                    """
                    self.server.close()
                
                else:   
                    self.request.send("Try again!!!!!\n")
                    continue
            
        

tcpServ = SocketServer.TCPServer(ADDR, MyRequestHandler)
tcpServ.allow_reuse_address = True
print 'waiting for connection....'
tcpServ.serve_forever()
        
        
    
    
