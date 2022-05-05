import os

# 请求超时=drop(与主机不在线状态一样，所以利用icmp来检测主机是否在线有bug)
# 无法连到端口=reject
import threading
import time

count = 0


def get_ip(i):
    global count
    ip_prefix = '192.168.150.'
    for p in i:
        ip = f"{ip_prefix}{p}"
        output = os.popen(f"ping -w 100 -n 1 {ip}").read()
        if 'TTL=' in output or '无法连到端口' in output:
            count += 1
            print(ip)


if __name__ == '__main__':
    ip_total = []
    for t in range(1, 256):
        ip_total.append(t)
    ip_list = []
    for l in range(0, 256, 10):  # 看需要分多少组
        ip_list.append(ip_total[l:l + 10])
    for ips in ip_list:
        threading.Thread(target=get_ip, args=(ips,)).start()
    time.sleep(7)
    print(f"共有{count}台主机在线")
