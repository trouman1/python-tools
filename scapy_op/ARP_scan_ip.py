import threading
from scapy.layers.l2 import ARP
from scapy.sendrecv import sr1
import logging

# 可以通过logging模块控制提示报错等级，只提示Error及以上级别的报错信息：
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def scapy_ip(p):
    for i in p:
        ip = f'192.168.150.{i}'
        try:
            pkg = ARP(psrc='192.168.0.101', pdst=ip)
            reply = sr1(pkg, timeout=2, verbose=False)
            print(f"{ip} 在线\nMAC:{reply[ARP].hwsrc}")
        except TypeError as t:
            pass


if __name__ == '__main__':
    ip_total = []
    for t in range(1, 256):
        ip_total.append(t)
    ip_list = []
    for l in range(0, 256, 10):  # 看需要分多少组
        ip_list.append(ip_total[l:l + 10])
    for ips in ip_list:
        threading.Thread(target=scapy_ip, args=(ips,)).start()
