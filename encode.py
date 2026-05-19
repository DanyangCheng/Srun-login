import hashlib
from xxtea import encode

def sha1_hash(input_string):
    sha1 = hashlib.sha1()

    sha1.update(input_string.encode('utf-8'))

    return sha1.hexdigest()


def encodeUserInfo(info, token):
    temp = encode(info, token)
    return "{SRBX1}" + base64encode(temp)


ALPHA='LVoJPiCN2R8G90yg+hmFHuacZ1OWMnrsSTXkYpUq/3dlbfKwv6xztjI7DeBE45QA'
PADCHAR = "="


def _getbyte(s, i):
    return ord(s[i])


def base64encode(s):
    if len(s) == 0:
        return s
    x = []
    imax = len(s) - len(s) % 3 


    for i in range(0, imax, 3):

        b10 = (_getbyte(s, i) << 16) | (_getbyte(s, i + 1) << 8) | _getbyte(s, i + 2)

        x.append(ALPHA[b10 >> 18])
        x.append(ALPHA[(b10 >> 12) & 63])
        x.append(ALPHA[(b10 >> 6) & 63])
        x.append(ALPHA[b10 & 63])

    if len(s) - imax == 1:
        b10 = _getbyte(s, imax) << 16
        x.append(ALPHA[b10 >> 18] + ALPHA[(b10 >> 12) & 63] + PADCHAR + PADCHAR)
    elif len(s) - imax == 2:
        b10 = (_getbyte(s, imax) << 16) | (_getbyte(s, imax + 1) << 8)
        x.append(
            ALPHA[b10 >> 18]
            + ALPHA[(b10 >> 12) & 63]
            + ALPHA[(b10 >> 6) & 63]
            + PADCHAR
        )

    return "".join(x)
