import base64

# source = 'H你'
# # 先将source转换成二进制，再对二进制进行base64编码，剩余的用“=”补齐
# dest = base64.b64encode(source.encode())
# print(dest.decode())

with open('../temp/1.png', mode='rb') as img1:
    content = img1.read()
    source = base64.b64encode(content)

with open('../temp/2.png', mode='wb') as img2:
    img2.write(base64.b64decode(source))
