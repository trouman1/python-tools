from scapy.all import *
import logging

# 可以通过logging模块控制提示报错等级，只提示Error及以上级别的报错信息：
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)


def do_monitor(flow):
    try:
        res = flow[Raw].load.decode().split('\n')  # 根据show()的结构查看详细数据
        # if res[0].startswith('GET') or res[0].startswith('POST'):
        #     print(res[0])  # 获取GET和POST的请求头

        print(res[-1])  # 获得正文内容

        # print(flow.summary)  # 大概的有标识信息
    except:
        pass


if __name__ == '__main__':
    sniff(filter="tcp and port 80", prn=lambda x: do_monitor(x))  # prn是回调函数,通常与lambda搭配使用
