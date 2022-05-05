import socket
import time


def feiq():
    packetid = str(time.time())
    name = "xll"
    host = "xll"
    command = str(0x00000020)
    content = "halo!world!"
    # 飞鸽传书的协议规则==版本号:包编号:发送者姓名:发送者主机名:命令字:附加信息
    message = "1.0:" + packetid + ":" + name + ":" + host + ":" + command + ":" + content
    send_message = message.encode()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('192.168.150.132', 2425))
    s.send(send_message)
    s.close()


if __name__ == '__main__':
    i = 0
    while i < 10:
        i += 1
        feiq()
