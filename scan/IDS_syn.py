import os
import time


def check_syn():
    blacklist = []  # 定义一个黑名单
    ip_suspicion = []  # 定义一个可疑ip名单
    SYN_RECV_sum = os.popen("netstat -ant | grep SYN_RECV | wc -l").read()  # 查看SYN_RECV报文是否有异常
    if int(SYN_RECV_sum) > 50:
        SYN_RECV_ip = os.popen(
            "netstat -ant | grep SYN_RECV | awk '{print $5}'|awk -F : '{print $1}'").readlines()  # 获取异常报文的IP
        for i in set(SYN_RECV_ip):
            ip_suspicion.append(i.split())
    for ip in ip_suspicion:
        ip = str(ip)[2:-2]
        if ip == '127.0.0.1':
            pass
        else:
            suspicion_count = os.popen(f"netstat -ant | grep SYN_RECV | grep {ip} |wc -l").read()  # 判断IP是否是攻击行为
            if int(suspicion_count) > 20:
                blacklist.append(ip)  # 如果属于攻击行为就加入黑名单
    return blacklist


def do_ids():
    blacklist = check_syn()
    for blackip in blacklist:
        try:
            os.popen(f"firewall-cmd --add-rich-rule='rule family=ipv4 source address={blackip} drop' --timeout=10m")
            print(f"检测到{blackip}正在攻击服务器，已拉黑10分钟")
        except:
            pass


if __name__ == '__main__':
    while True:
        do_ids()
        time.sleep(1)
