import hashlib


# 不可逆加密（根据密文无法解密）
def md5(text):
    text_md5 = hashlib.md5(text.encode()).hexdigest()  # 对二进制进行加密
    print(text_md5)


def sha(text):
    text_sha = hashlib.sha512(text.encode()).hexdigest()
    print(text_sha)


# hash.digest() 返回摘要，作为二进制数据字符串值
# hash.hexdigest() 返回摘要，作为十六进制数据字符串值

if __name__ == '__main__':
    source = '你好'
    md5(source)
    sha(source)
