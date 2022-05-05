# 栅栏密码:先将密文分为两行,再按上下上下的顺序组合成一句话


def encrypt(string):
    plaintext = string
    ciphertext1 = ''
    ciphertext2 = ''
    for i in range(len(plaintext)):
        if (i % 2) == 0:  # 取余
            ciphertext1 += plaintext[i]  # 第一位下标为0给text1,第二位下标为1给text2，依次下来2——》text1，3——》text2
        else:
            ciphertext2 += plaintext[i]
    ciphertexts = [ciphertext1, ciphertext2]
    return ciphertexts


def decrypt(ciphertext1, ciphertext2):  # 解密函数 ，输入密文1，密文2
    plaintext = ''
    for i in range(len(ciphertext1)):
        plaintext += ciphertext1[i]
        if i < len(ciphertext2):
            plaintext += ciphertext2[i]
    return plaintext


if __name__ == '__main__':
    ciphertext = encrypt('ni shi zhu ba bu ran ni wei shen me zhe me ben!')
    print(ciphertext)
    # print(decrypt(ciphertext[0], ciphertext[1]))
