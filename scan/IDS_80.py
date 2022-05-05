import os
import time
from collections import Counter


def get_cpu_load():  # 获取CPU一分钟内的平均负载，砍掉（反应太慢，影响判断）
    cpu_load = float(os.popen("uptime | awk -F ': ' '{print $2}' | awk -F ',' '{print $1}'").read())
    # print('cpu:', cpu_load)
    return cpu_load


def get_conn_count():  # 获取netstat -ant的连接数量
    conn_count = int(os.popen('netstat -ant | wc -l').read())
    # print('coon:', conn_count)
    return conn_count


def get_syn_recv():  # 获取recv报文的数量
    recvq = int(os.popen("ss -lnt | grep :80 | awk '{print $2}'").read())
    # print('recv:', recvq)
    return recvq


def get_net_bandwidth():  # 获取接收流量，取十次，得平均数
    # flow = int(os.popen("ifconfig ens33 | grep 'RX packets' | awk '{printf $5}'").read())
    flow_10 = []
    subtraction = []
    for i in range(10):
        flow_sum = int(os.popen("ifconfig ens33 | grep 'RX packets' | awk '{printf $5}'").read())
        flow_10.append(flow_sum)
        time.sleep(0.1)
    for f in range(len(flow_10)):
        if f != 9:
            i = flow_10[f + 1] - flow_10[f]
            subtraction.append(i)
        else:
            pass
    average = (subtraction[0] + subtraction[1] + subtraction[2] + subtraction[3] + subtraction[4] + subtraction[5] +
               subtraction[6] + subtraction[7] + subtraction[8]) / 9
    # print(int(average))
    return int(average)


def get_most_ip():  # 获取连接数最多的IP
    ip_list = os.popen("netstat -ant | grep :80 | awk '{print $5}'").read().split('\n')
    count_ip = []
    for c_ip in ip_list:
        count_ip.append(c_ip.split(':')[0])
    rank = Counter(count_ip)
    most_ip = rank.most_common()
    # print(most_ip[0][0])
    return most_ip[0][0]


def join_the_blacklist(i):  # 加入防火墙黑名单
    os.popen(f"firewall-cmd --add-rich-rule='rule family=ipv4 source address={i} drop' --timeout=10m")
    print(f"检测到{i}正在攻击服务器，已拉黑10分钟")


if __name__ == '__main__':
    while True:
        conn = get_conn_count()
        recv = get_syn_recv()
        flow = get_net_bandwidth()
        print(f"TCP Conn: {conn}, REVC_SYN: {recv}, Flow: {flow}")
        if conn > 500 and recv > 50 and flow > 5000:
            ip = get_most_ip()
            join_the_blacklist(ip)
        time.sleep(5)
