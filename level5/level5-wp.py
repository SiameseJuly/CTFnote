import gmpy2

def ascii2str(strs):
    result = ""
    if (len(strs) % 2) == 0:
        strs = strs[2:]
    else:
        strs = strs[2:]
        strs = '0' + strs
    for i in range(0,len(strs),2):
        single_str=chr(int((strs[i:(i+2)]),16))
        result="%s%s"%(result,single_str)
    print result    
    return result

with open('flag.enc','r') as f:
    ciphertext = f.read()
    
ciphertext = gmpy2.mpz('0x'+ciphertext.encode('hex'))

N = 0xC2636AE5C3D8E43FFB97AB09028F1AAC6C0BF6CD3D70EBCA281BFFE97FBE30DD 
N = gmpy2.mpz(N)

e = 2

p = gmpy2.mpz(275127860351348928173285174381581152299)
q = gmpy2.mpz(319576316814478949870590164193048041239)
              

mp = gmpy2.powmod(ciphertext,(p+1)/4,p)
mq = gmpy2.powmod(ciphertext,(q+1)/4,q)
yp = gmpy2.invert(p,q)
yq = gmpy2.invert(q,p)

a = (yp*p*mq + yq*q*mp)%N
b = N - int(a)
c = (yp*p*mq - yq*q*mp)%N
d = N - int(c)

print ascii2str(hex(d))
