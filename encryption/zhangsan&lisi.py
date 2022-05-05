import string


def zhangsan_encrypt(text):  # 张三的加密算法是：采用凯撒加密算法，字母右移5位
    i_acsii, res = '', ''
    for i in text:
        if ord(i) in range(86, 91) or ord(i) in range(118, 123):  # 如果在[w,x,y,z,W,X,Y,Z]中
            i_acsii = ord(i) - 21
        elif i in string.ascii_letters:  # 如果是字母
            i_acsii = ord(i) + 5
        else:
            i_acsii = ord(i)
        res += chr(i_acsii)
    return res


def zhangsan_decrypt(text):  # 张三的解密算法是：采用凯撒加密算法，字母左移5位
    i_acsii, res = '', ''
    for i in text:
        if ord(i) in range(65, 70) or ord(i) in range(97, 102):  # 如果在[a,b,c,d,A,B,C,D]中
            i_acsii = ord(i) + 21
        elif i in string.ascii_letters:  # 如果是字母
            i_acsii = ord(i) - 5
        else:
            i_acsii = ord(i)
        res += chr(i_acsii)
    return res


def lisi(text):  # 李四的加密算法是：大小写互换
    i_acsii, res = '', ''
    for i in text:
        if i in string.ascii_lowercase:  # 如果是小写字母
            i_acsii = ord(i) - 32
        elif i in string.ascii_uppercase:  # 如果是大写字母
            i_acsii = ord(i) + 32
        else:
            i_acsii = ord(i)
        res += chr(i_acsii)
    return res


if __name__ == '__main__':
    source = 'FuckUSA'
    print(source+'\t源')
    zhangsan_en = zhangsan_encrypt(source)
    print(zhangsan_en+'\t由张三加密发送给李四')
    lisi_en = lisi(zhangsan_en)
    print(lisi_en+'\t李四加密发送给张三')
    zhangsan_de = zhangsan_decrypt(lisi_en)
    print(zhangsan_de+'\t张三解密发送给李四')
    lisi_de = lisi(zhangsan_de)
    print(lisi_de+'\t李四解密后得到源')
    # 在此次通信中，双方传输的都是经过加密的信息，这种方法成为非对称加密
