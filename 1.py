# -*- coding: utf-8 -*
import SocketServer 
from time import ctime

import flag

HOST = ''

PORT = 21567

ADDR = (HOST,PORT)
signal = """
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
                self.request.send("Please submit the Flag:\n")  
                result  = self.request.recv(1024)[:-1]
                
                if result == flag.flag1 :
                    
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
                self.request.send("if you get the m,give me directly halfbit{} !\n")
                self.request.send("c = 0xdc2eeeb2782c\n")
                self.request.send("N = 322831561921859\n")
                # p =13574881
                # q = 23781539
                self.request.send("e = 23\n")
                self.request.send("Please submit the Flag:\n")     
                result  = self.request.recv(1024)[:-1]
                
                if result == flag.flag2 :
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
                self.request.send("c1 = 0x1b19e2c03eef1d467ee942b63826cd122695e4698c787250f1d215f3390470512e70ad5eb49ae64fa2481fe84aa962a587f1be356428d373ad6c45433d52acc6330aea207328b78dc51b392bdcb81195d9ee72bc6b4ee113f37735964415a5410e674b7409e4b063729217259af0f9d0496ac24ef55f768bff36916eb3f162aeaa3ac0583ba26d0df4d3c4dffd009062e0d7699ecf23373091e6fa0d6b5b40e47c9660313706e26d1d45bd40b787aecdc37d6e59886173ad56408f99a5efea132592f594d9101d96cd827422a874265fe1b5a265a\n")
                self.request.send("c2 = 0x15317d73a321371d33a73b0e6b601d9a368d5e92551828b5eebb94d789afc5e55f5bbf097565328b13669bc22083bddb3ac33e58b514c990ff83b8b48720612aa31586f39071adda45490b3fd64620ec82038931020624f69fa2557c1dfdb8a9d1e31fad025def33326293db424561e650d444df58a58b013823e08f9102671bd12c2498c8531321937d47f52edda0ce73281c703f98354e9440fc76e91a3e6d7a8cd2913436bdc5c889891471a9cb1bc708d89539159140c9dd28e2c8647ec925d17cea0f0f6a36285019998c0667e38c8cdb4c2\n")
                self.request.send("e = 65537\n")
                self.request.send("Please submit the Flag:\n")                
                result  = self.request.recv(1024)[:-1]
                
                if result == flag.flag3 :
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
                self.request.send("N = 0xace2aa1121d22a2153389fba0b5f3e24d8721f5e535ebf5486a74191790c4e3cdd0316b72388e7de8be78483e1f41ca5c930df434379db76ef02f0f8cd426348b62c0155cdf1d5190768f65ce23c60a4f2b16368188954342d282264e447353c62c10959fee475de08ec9873b84b5817fecb74899bedde29ef1220c78767f4de11ef1756404494ae1ce4af184cbc1c7c6de8e9cd16f814bca728e05bc56b090112f94fff686bf8122a3b199eb41080860fa0689ed7dbc8904184fb516b2bbf6b87a0a072a07b9a26b3cda1a13192c03e24dec8734378d10f992098fe88b526ce70876e2c7b7bd9e474307dc6864b4a8e36e28ce6d1b43e3ab5513baa6fa559ff\n")
                self.request.send("e1 = 0xac8b\n")
                self.request.send("c1 = 0x17af1d865c682e3d071c9cebb3f83e9784fec1189c91c6ee8c95c11d051bfbd8c9b77b87bd792e88bf0c9cd5251b7ea88fb3dff8432d9ce96bbde536febe27603f06bfe5b430ca1f3f4fb53a4bb51c26809426a56f57ad30406d2a7699f8fe9aeb50cb48344a96d845f6e6fb8cd21708e174fe5dba701b5f1ab7d6739609f3c1fc491a65a529438e2734dec7d1d24099829292de4ab4d308df794387777e5930d2477eaa21270516ffa2cf738f057dc037e27548eec2a0ed434b496b8ce85d2e7b8bf8e72ba9e69f18e5d3f71123412a34972ea985a8b2e6bfa7603b6afbf831157c4ee8eb914356bafac2d4383344cdf26fc4ce3efed6220a841afd03d38fed\n")                
                self.request.send("e2 = 0x1091\n")
                self.request.send("c2 = 0x4a03fdf2b92cf28f4f05c6778f828cb2086cfb4b880c8953ed54b36515fa05651107267177ba674c0468a1e069d33ca3094bd0f89dc3e0fccc4f3223608682e4f4526871d0b9b879504f25144864aad3845d83acfd6ed207f3fa573a6c32ad71563a5fe3f86a72a5ecc29519880b910258060d3f01995600e52414832efb01248c7daa33fed6250d03771b11e0a3fc42bf8f3bb858ebfd136ceb988812efafa826ffc5a53337af9feb593e8a4071489732d42727086df0945d0dd5ea97267a3c501a6f6160d165f006d9f1320982046409c5d816143b841fbc4f9104ae86419cdf70a510b4b3f5f5a96215d80f8a67ee2c43d0227ec7daa34b2a6b4a2ae6083c\n")
                self.request.send("Please submit the Flag:\n")
                result  = self.request.recv(1024)[:-1]
                
                if result == flag.flag4 :
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
                self.request.send("Download the file: https://static2.ichunqiu.com/icq/resources/fileupload/phrackCTF/CRYPTO/extremelyhardRSA.rar")
                self.request.send("if you get the m,give me directly !\n")
                self.request.send("Maybe is not like halfbit{********}\n")
                self.request.send("Please submit the Flag:\n")
                result  = self.request.recv(1024)[:-1]
                
                if result == flag.flag5 :
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
                self.request.send("Download the file:  https://static2.ichunqiu.com/icq/resources/fileupload/phrackCTF/CRYPTO/hardRSA.rar\n")
                self.request.send("if you get the m,give me directly !\n")
                self.request.send("Maybe is not like halfbit{********}\n")
                self.request.send("Please submit the Flag:\n")
                result  = self.request.recv(1024)[:-1]
                
                if result == flag.flag6 :
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
                self.request.send("n1 = 0x43d819a4caf16806e1c540fd7c0e51a96a6dfdbe68735a5fd99a468825e5ee55c4087106f7d1f91e10d50df1f2082f0f32bb82f398134b0b8758353bdabc5ba2817f4e6e0786e176686b2e75a7c47d073f346d6adb2684a9d28b658dddc75b3c5d10a22a3e85c6c12549d0ce7577e79a068405d3904f3f6b9cc408c4cd8595bf67fe672474e0b94dc99072caaa4f866fc6c3feddc74f10d6a0fb31864f52adef71649684f1a72c910ec5ca7909cc10aef85d43a57ec91f096a2d4794299e967fcd5add6e9cfb5baf7751387e24b93dbc1f37315ce573dc063ecddd4ae6fb9127307cfc80a037e7ff5c40a5f7590c8b2f5bd06dd392fbc51e5d059cffbcb85555\n")
                self.request.send("c1 = 0x270004408a0f9085316cd605e152225eb4486138f7d7e701f586716faf6054146432e502a92f5eb0451383e99b1bc5f0afb337389218ec4db61fa8ada9aea93ef8a30958ea72ed04178abaf833ed071d3290c2815caa1a99fa4b30ee96a3d9a664544613b26a3dbc60627b762fbc7cbc06d584b42ccea636606566f5a17e4f135f7cff5b08c05f33c0ad48f3d39a1797f047ea50f4fea4783d39f971e2d735ff1efc7f1fc690c04657f731917e90e6687644d5db643427e488114a26b7ff31884ce70bedc0620516aab82eb567f636ba67dc642d09688f03b0fa516f9e7f7e27b89174da0ca05438bb280848fb0457a0e1491cc0d7a80dd17e73204437146d71\n")
                self.request.send("n2 = 0x60d175fdb0a96eca160fb0cbf8bad1a14dd680d353a7b3bc77e620437da70fd9153f7609efde652b825c4ae7f25decf14a3c8240ea8c5892003f1430cc88b0ded9dae12ebffc6b23632ac530ac4ae23fbffb7cfe431ff3d802f5a54ab76257a86aeec1cf47d482fec970fc27c5b376fbf2cf993270bba9b78174395de3346d4e221d1eafdb8eecc8edb953d1ccaa5fc250aed83b3a458f9e9d947c4b01a6e72ce4fee37e77faaf5597d780ad5f0a7623edb08ce76264f72c3ff17afc932f5812b10692bcc941a18b6f3904ca31d038baf3fc1968d1cc0588a656d0c53cd5c89cedba8a5230956af2170554d27f524c2027adce84fd4d0e018dc88ca4d5d26867\n")                
                self.request.send("c2 = 0x218b37071a30e6276e543c9f0a2f4a1d8d61a10afba951fa33df6e705388b8b8b6a6c468b7643088a6ffed56f3e3a58c05195942d40d231fcd1ab4775c9c0f3beb10d38d736e1c1f3d093b16ce934e7fd3422f3fc66360eec34b9800ff78d07c1a0bb53cfbe4ecb36724f1bcb69e25b50ad6df3ea8a7864de223ca48540dec8c77be550b9548b6f2c481d8ebaec2b9cdb1ce985e0c48914c436f895571396085c7473bc19259a0f9fd4602718e8c4a52695ed392729104af211b9ffef2324ce738e18f8bd7ae8205181d63048b41625f1ef0d6a4743331e42c41cf19b48c92a3185049dc8cec17f914b4dd2acf1659c1a3764f9d2d38063dfe0896b547c0cf72\n")
                self.request.send("n3 = 0x280f992dd63fcabdcb739f52c5ed1887e720cbfe73153adf5405819396b28cb54423d196600cce76c8554cd963281fc4b153e3b257e96d091e5d99567dd1fa9ace52511ace4da407f5269e71b1b13822316d751e788dc935d63916075530d7fb89cbec9b02c01aef19c39b4ecaa1f7fe2faf990aa938eb89730eda30558e669da5459ed96f1463a983443187359c07fba8e97024452087b410c9ac1e39ed1c74f380fd29ebdd28618d60c36e6973fc87c066cae05e9e270b5ac25ea5ca0bac5948de0263d8cc89d91c4b574202e71811d0ddf1ed23c1bc35f3a042aac6a0bdf32d37dede3536f70c257aafb4cfbe3370cd7b4187c023c35671de3888a1ed1303\n")
                self.request.send("c3 = 0x15756c5884f272a92d8434f13bcf98e6029c6a51dd57d6ee899115c5d19879e4daf7be85d63fd1b2a69647c8d1cf40b7d3856ac9120f2bba861fa663c85b5af25c7bf48481d5799fa6c5bf62e5617b1f6f899a9b50652aeeb5b93ca3df954422f95794126459d499d8cc7def5bf5c6019adfbd29e5d04f3936f6421ec6e703dffa3b9b6f04e73ca75abf034d5acea877c38df6da674124ca7890a0ccdaca4b04e0d7662e230bf8bd52ee66f6a121b733ab32564a2aaaaf297982bc912afd5790d839580443dc77e6f22e90e38c8dae464ca64505601d3a2b015f9ae1bb15d978f013e3dfe5ad7bfbaaa2e5e78c6609710d17b5c7bf485b22f6dd39c3344869ac\n")
                self.request.send("Please submit the Flag:\n")
                
                result  = self.request.recv(1024)[:-1]
                
                if result == flag.flag7 :
                    goal = 7
                    self.request.send("Correct !\n")
                    self.request.send("Congratulatios! You have finished the basical RSA lessons!!!!\n")
                    print signal
                    self.request.send(signal)
                    self.server.close()
                
                else:   
                    self.request.send("Try again!!!!!\n")
                    continue
            
        

tcpServ = SocketServer.TCPServer(ADDR, MyRequestHandler)
tcpServ.allow_reuse_address = True
print 'waiting for connection....'
tcpServ.serve_forever()
        
        
    
    
