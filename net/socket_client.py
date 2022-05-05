import socket


# # 模拟客户端
# def client():
#     client1 = socket.socket()
#     client1.connect(('192.168.18.5', 9999))  # 连接得是元组
#     while True:
#         send_message = input("请输入你要发送的信息：")
#         client1.send(send_message.encode())  # 用send发送信息
#         get_message = client1.recv(1024000).decode()  # 接收信息
#         print(f"你收到一条信息：\n{get_message}")

# 模拟客户端
def client():
    client1 = socket.socket()
    client1.connect(('192.168.150.219', 9999))  # 连接得是元组
    while True:
        send_message = input("请输入你要发送的信息：")
        client1.send(send_message.encode())  # 用send发送信息
        get_message = client1.recv(1024000).decode()  # 接收信息
        print(f"你收到一条信息：\n{get_message}")


if __name__ == '__main__':
    client()
