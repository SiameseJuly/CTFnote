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

N = 322831561921859
p = 13574881
q = 23781539
c = 0xdc2eeeb2782c
e = 23

phi = (p-1)*(q-1)
d =gmpy2.invert(e, phi)

flag = gmpy2.powmod(c, d, N)

asc2str(hex(flag))