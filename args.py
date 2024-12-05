import argparse

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--username',type=str,default="",help="your user name.")
    parser.add_argument('--passwd',type=str,default="",help="your password.")
    parser.add_argument('--login_host',type=str,default="",help="login host.")
    args = parser.parse_args()
    return args