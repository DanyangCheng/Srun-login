import hashlib
import hmac
def md5(passwd, token=None, raw=False):
    if passwd is None:
        passwd = ""
    content_bytes = str(passwd).encode('utf-8')
    if token:
        key_bytes = str(token).encode('utf-8')
        hasher = hmac.new(key_bytes, content_bytes, hashlib.md5)
        digest = hasher.digest()
    else:
        hasher = hashlib.md5(content_bytes)
        digest = hasher.digest()
    if raw:
        return digest
    else:
        return digest.hex()