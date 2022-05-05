from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex

source = '你好世界!'

# 如果source不足16位的倍数就用空格补足为16位
if len(source.encode('utf-8')) % 16:
    add = 16 - len(source.encode('utf-8')) % 16
else:
    add = 0
source = source + '\0' * add

# 定义密钥和偏移量，必须是16个字节、24字节或32字节
key = 'todayiswonderful-FEDCBA987654321'.encode()
mode = AES.MODE_CBC
iv = b'1234567890ABCDEF'
cryptos = AES.new(key, mode, iv)

# 进行加密处理
# cipher = cryptos.encrypt(source.encode())
# print(b2a_hex(cipher).decode())  # 便于传播可以将其转换成16进制，

# 解密
msg = '9069e26312c7b055dcd69689a5891d98'
dest = cryptos.decrypt(a2b_hex(msg))
print(dest.decode().strip('\0'))
