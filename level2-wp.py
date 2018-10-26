import gmpy2


def asc2str(strs):
    result = ''
    if (len(strs) % 2) == 0 :
        strs = strs[2:]
    else:
        strs = strs[2:]
        strs = '0' + strs
    result = strs.decode('hex')
    print result
    return result

N1 = gmpy2.mpz(9051013965404084482870087864821455535159008696042953021965631089095795348830954383127323853272528967729311045179605407693592665683311660581204886571146327720288455874927281128121117323579691204792399913106627543274457036172455814805715668293705603675386878220947722186914112990452722174363713630297685159669328951520891938403452797650685849523658191947411429068829734053745180460758604283051344339641429819373112365211739216160420494167071996438506850526168389386850499796102003625404245645796271690310748804327)
N2 = gmpy2.mpz(13225948396179603816062046418717214792668512413625091569997524364243995991961018894150059207824093837420451375240550310050209398964506318518991620142575926623780411532257230701985821629425722030608722035570690474171259238153947095310303522831971664666067542649034461621725656234869005501293423975184701929729170077280251436216167293058560030089006140224375425679571181787206982712477261432579537981278055755344573767076951793312062480275004564657590263719816033564139497109942073701755011873153205366238585665743)

c1 = gmpy2.mpz(0x1b19e2c03eef1d467ee942b63826cd122695e4698c787250f1d215f3390470512e70ad5eb49ae64fa2481fe84aa962a587f1be356428d373ad6c45433d52acc6330aea207328b78dc51b392bdcb81195d9ee72bc6b4ee113f37735964415a5410e674b7409e4b063729217259af0f9d0496ac24ef55f768bff36916eb3f162aeaa3ac0583ba26d0df4d3c4dffd009062e0d7699ecf23373091e6fa0d6b5b40e47c9660313706e26d1d45bd40b787aecdc37d6e59886173ad56408f99a5efea132592f594d9101d96cd827422a874265fe1b5a265a)
c2 = gmpy2.mpz(0x15317d73a321371d33a73b0e6b601d9a368d5e92551828b5eebb94d789afc5e55f5bbf097565328b13669bc22083bddb3ac33e58b514c990ff83b8b48720612aa31586f39071adda45490b3fd64620ec82038931020624f69fa2557c1dfdb8a9d1e31fad025def33326293db424561e650d444df58a58b013823e08f9102671bd12c2498c8531321937d47f52edda0ce73281c703f98354e9440fc76e91a3e6d7a8cd2913436bdc5c889891471a9cb1bc708d89539159140c9dd28e2c8647ec925d17cea0f0f6a36285019998c0667e38c8cdb4c2)
a,b,c = gmpy2.gcdext(N1, N2)

p1 = N1/a
p2 = N2/a
q = a 

e1 =65537
e2 = 17

phi1 = (p1-1)*(q-1)
phi2 = (p2-1)*(q-1)
d1 =gmpy2.invert(e1, phi1)
d2 =gmpy2.invert(e2, phi2)


flag1 = gmpy2.powmod(c1, d1, N1)
flag2 = gmpy2.powmod(c2, d2, N2)

c1 =asc2str(hex(flag1))
c2 =asc2str(hex(flag2))


#m1 ="halfbit{Modules_"
#m2 ="should_be_prime}"

#c1 = gmpy2.powmod(int(m1.encode('hex'),16),e1,N1)
#c2 = gmpy2.powmod(int(m2.encode("hex"),16),e2,N2)
#print hex(c1)
#print hex(c2)