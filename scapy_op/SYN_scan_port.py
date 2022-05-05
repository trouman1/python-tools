import threading
from scapy.layers.inet import IP, TCP
from scapy.sendrecv import sr1
import logging

# 可以通过logging模块控制提示报错等级，只提示Error及以上级别的报错信息：
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


# 基于半连接 S / SA / RA 等标志位来对端口进行判断
# 如果目标端口开放，则S->SA，如果目标端口未开放，则S->RA
def scapy_port(ip, p):
    for port in p:
        try:
            # 通过指定源IP地址，可以实现IP欺骗，进而导致半连接，此类操作也可以用于Flags参数定义上
            pkt = IP(dst=ip) / TCP(dport=port, flags='S')  # S=SYN
            reply = sr1(pkt, timeout=1, verbose=False)
            if int(reply[TCP].flags) == 18:  # 18==0x12==SYN+ACK
                print(f'端口 {port} 开放')
        except TypeError as e:
            # print(e)
            pass


if __name__ == '__main__':
    port_total = []
    for t in range(1, 65536):
        port_total.append(t)
    port_list = []
    for l in range(0, 65536, 500):  # 看需要分多少组
        port_list.append(port_total[l:l + 500])
    for ports in port_list:
        threading.Thread(target=scapy_port, args=('192.168.150.132', ports,)).start()
