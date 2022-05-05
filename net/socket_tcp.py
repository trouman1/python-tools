import socket

# 模拟客户端
str1 = "777".encode()  # 将字符串类型转换成二进制
ss = socket.socket()
ss.connect(('192.168.18.6', 9898))  # 连接得是元组
ss.send(str1)
ss.close()

# 模拟服务端
s = socket.socket()
s.bind(('192.168.18.5', 555))
s.listen()
while True:
    val, addr = s.accept()
    value = val.recv(1024)
    print(value.decode())
