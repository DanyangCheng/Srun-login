import math

def s(a, b):
    c = len(a)
    v = []
    for i in range(0, c, 4):
        val = 0
        if i < c:     val |= ord(a[i])
        if i + 1 < c: val |= (ord(a[i + 1]) << 8)
        if i + 2 < c: val |= (ord(a[i + 2]) << 16)
        if i + 3 < c: val |= (ord(a[i + 3]) << 24)
        v.append(val & 0xFFFFFFFF)
    
    if b:
        v.append(c)
    return v

def l(a, b):
    d = len(a)
    c = (d - 1) << 2

    if b:
        m = a[-1]
        if m < c - 3 or m > c:
            return None
        c = m

    res = []
    for i in range(d):
        val = a[i]
        res.append(chr(val & 0xff))
        res.append(chr((val >> 8) & 0xff))
        res.append(chr((val >> 16) & 0xff))
        res.append(chr((val >> 24) & 0xff))

    res_str = "".join(res)
    return res_str[:c] if b else res_str

def encode(string, key):
    if not string:
        return ''
        
    v = s(string, True)
    k = s(key, False)
    
    while len(k) < 4:
        k.append(0)
        
    n = len(v) - 1
    z = v[n]
    y = v[0]
    
    c = 0x9E3779B9 
    q = math.floor(6 + 52 / (n + 1))
    d = 0

    while q > 0:
        q -= 1
        d = (d + c) & 0xFFFFFFFF
        e = (d >> 2) & 3

        for p in range(n):
            y = v[p + 1]
            # m = z >>> 5 ^ y << 2;
            term1 = (z >> 5) ^ ((y << 2) & 0xFFFFFFFF)
            # m += y >>> 3 ^ z << 4 ^ (d ^ y);
            term2 = (y >> 3) ^ ((z << 4) & 0xFFFFFFFF) ^ (d ^ y)
            m = term1
            m = (m + term2) & 0xFFFFFFFF
            # m += k[p & 3 ^ e] ^ z;
            m = (m + (k[(p & 3) ^ e] ^ z)) & 0xFFFFFFFF
            
            v[p] = (v[p] + m) & 0xFFFFFFFF
            z = v[p]

        p = n
        y = v[0]
        term1 = (z >> 5) ^ ((y << 2) & 0xFFFFFFFF)
        term2 = (y >> 3) ^ ((z << 4) & 0xFFFFFFFF) ^ (d ^ y)
        m = term1
        m = (m + term2) & 0xFFFFFFFF
        m = (m + (k[(p & 3) ^ e] ^ z)) & 0xFFFFFFFF
        
        v[n] = (v[n] + m) & 0xFFFFFFFF
        z = v[n]

    return l(v, False)