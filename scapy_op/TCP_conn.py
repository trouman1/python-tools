import random
import time

from scapy.layers.inet import TCP, IP
from scapy.sendrecv import sr1, send
import logging

# 可以通过logging模块控制提示报错等级，只提示Error及以上级别的报错信息：
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def tcp_conn(text):
    first_seq = random.randint(1, 99999)
    sport = random.randint(10000, 20000)
    dport = 554
    dst = '192.168.18.39'
    # src = '192.168.18.20'  # 可以定义假的src地址，如果不定义的话默认用本机
    # sr1和sr的区别在于sr1返回的只有应答包，没有未应答包。

    # 三次握手
    SYN = sr1(IP(dst=dst) / TCP(sport=sport, dport=dport, seq=first_seq, flags="S"), timeout=1)  # SYN
    ack_3 = SYN[TCP].seq + 1
    seq_3 = SYN[TCP].ack
    sr1(IP(dst=dst) / TCP(sport=sport, dport=dport, seq=seq_3, ack=ack_3, flags="A"), timeout=1)  # ACK

    # 发送信息
    MSG = sr1(IP(dst=dst) / TCP(sport=sport, dport=dport, seq=seq_3, ack=ack_3, flags="PA") / text)  # PSH+ACK

    # 四次挥手
    FIN = IP(dst=dst) / TCP(sport=sport, dport=dport, flags="FA", seq=MSG[TCP].ack, ack=MSG[TCP].seq)  # FIN+ACK
    FINACK = sr1(FIN, timeout=1)
    time.sleep(1)
    LASTACK = IP(dst=dst) / TCP(sport=sport, dport=dport, flags="A", seq=FINACK.ack, ack=FINACK.seq + 1)  # ACK
    send(LASTACK)


if __name__ == '__main__':
    tcp_conn('halo')
