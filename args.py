import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username',type=str,default="24451352007",help="your user name.")
    parser.add_argument('--passwd',type=str,default="c*1764398966",help="your password.")
    parser.add_argument('--login_host',type=str,default="192.168.16.66",help="login host.")
    parser.add_argument('--ip',type=int,default="",help="your ip.")# 局域网ip
    args = parser.parse_args()
    return args