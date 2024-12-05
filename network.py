import netifaces
def get_ip():
    interfaces = netifaces.interfaces()
    for interface in interfaces:
        addrs = netifaces.ifaddresses(interface)
        if netifaces.AF_INET in addrs:
            ip_address = addrs[netifaces.AF_INET][0]['addr']
            if ip_address != "127.0.0.1":  # 忽略回环地址
                break
    return ip_address
