import requests
import json
import re
from urllib.parse import quote
from jQuery import jquery_mock_callback, get_current_timestamp
from encode import md5, encodeUserInfo, sha1_hash
from network import get_ip
from args import parse_args

jQuery = jquery_mock_callback()  # 模拟jQuery call back.


Head = {
    "Host": "192.168.16.66",
    "Connection": "keep-alive",
    "Accept": "text/javascript, application/javascript, application/ecmascript, application/x-ecmascript, */*; q=0.01",
    "X-Requested-With": "XMLHttpRequest",
    "Accept-Encoding": "gzip, deflate",
    "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6,cy;q=0.5",
    "Cookie": "lang=zh-CN",
}

def main(args):
    Username = args.username
    Passwd = args.passwd
    Host = args.login_host
    if Username =="":
        Username = input("Please enter your username:")
    if Passwd == "":
        Passwd = input("Please input your password:")
    if Host == "":
        Host = input("Please enter login host:")

    get_challenge_url = f"http://{Host}/cgi-bin/get_challenge?callback={jQuery}&username={Username}&ip={get_ip()}&_={str(get_current_timestamp())}"
    response = requests.get(get_challenge_url, headers=Head)  # 返回json
    json_data_str = re.sub(r"^[\w.]*\(","", response.text)
    json_data_str = json_data_str.rstrip(");")
    data = json.loads(json_data_str)
    token = data["challenge"]  # 提取challenge token


    hmd5 = md5(Passwd, token)  # 对passwd和token md5

    info = f'"username":"{Username}","password":"{Passwd}","ip":"{get_ip()}","acid":"2","enc_ver":"srun_bx1"'
    info = "{" + info + "}"

    i = encodeUserInfo(info, token)
    s = token + Username
    s += token + hmd5
    s += token + "2"#
    s += token + get_ip()
    s += token + "200"#
    s += token + "1"# 
    s += token + i# Encoded user info.

    checksum = sha1_hash(s)  # 计算用户信息和密码的校验和
    #TOD : os,name,double_stack,ac_id,n,tyoe
    login_url = f"http://{Host}/cgi-bin/srun_portal?callback={jQuery}&action=login&username={Username}&password=%7BMD5%7D{hmd5}&os=linux&name=Linux&nas_ip=&double_stack=0&chksum={checksum}&info={quote(i).replace('/','%2F')}&ac_id=2&ip={get_ip()}&n=200&type=1&captchaVal=&_={get_current_timestamp()}"
    response = requests.get(login_url, headers=Head)  # 发送登录信息
    print(response.text)


if __name__ == "__main__":
    
    args = parse_args()
    main(args)