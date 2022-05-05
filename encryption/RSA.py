import rsa

source = '你好世界'

public, private = rsa.newkeys(265)  # 第一步：生成公钥和私钥对，指定密钥的长度（越长越难破解）
print(public)
print(private)

encrypt = rsa.encrypt(source.encode(), public)  # 第二步：使用公钥加密
print(encrypt)

decrypt = rsa.decrypt(encrypt, private)  # 第三步：使用私钥解密
print(decrypt)

print(decrypt.decode())  # 第四步：输出密文 注意:encode与decode配对使用

# HTTPS通讯过程
# 用RSA对AES的密钥进行加密，然后用RSA解密得到AES的密钥
# 剩下的用AES对数据进行加解密传输
