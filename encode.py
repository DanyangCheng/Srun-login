import execjs
import hashlib
with open("./encode.js", "r") as file1,open("./md5.js","r") as file2:
    js_script = file1.read()
    encode_context = execjs.compile(js_script)
    js_script = file2.read()
    md5_context = execjs.compile(js_script)

def sha1_hash(input_string):
    # 创建一个 SHA-1 哈希对象
    sha1 = hashlib.sha1()

    # 更新哈希对象，传入数据。注意：数据必须是字节类型
    sha1.update(input_string.encode('utf-8'))

    # 获取最终的 SHA-1 哈希值（十六进制字符串）
    return sha1.hexdigest()

def md5(passwd, token):
    return md5_context.call("md5", passwd, token)


def encodeUserInfo(info, token):
    temp = encode_context.call("encode", info, token)
    return "{SRBX1}" + base64encode(temp)


ALPHA='LVoJPiCN2R8G90yg+hmFHuacZ1OWMnrsSTXkYpUq/3dlbfKwv6xztjI7DeBE45QA'
PADCHAR = "="  # 填充字符


def _getbyte(s, i):
    """获取字符串 s 中第 i 个字符的 ASCII 值"""
    return ord(s[i])


def base64encode(s):
    """Base64 编码"""
    if len(s) == 0:
        return s

    # 将输入的字符串转换为字符数组（已经是字符串类型）
    x = []
    imax = len(s) - len(s) % 3  # 计算最多能够分为 3 字符一组的部分

    # 遍历字符串，以 3 字符一组进行编码
    for i in range(0, imax, 3):
        # 计算 3 个字符拼接后的 24 位整数
        b10 = (_getbyte(s, i) << 16) | (_getbyte(s, i + 1) << 8) | _getbyte(s, i + 2)

        # 分别提取 6 位并映射到 Base64 字符集
        x.append(ALPHA[b10 >> 18])
        x.append(ALPHA[(b10 >> 12) & 63])
        x.append(ALPHA[(b10 >> 6) & 63])
        x.append(ALPHA[b10 & 63])

    # 处理剩下的 1 或 2 个字符
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
