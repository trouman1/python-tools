import string


def encryption(str1):  # 加密过程：大写变小写，小写变大写，数字+1
    i_acsii, res = '', ''
    for i in str1:
        if i in string.digits:  # 如果是数字
            i_acsii = ord(i) + 1
        elif i in string.ascii_lowercase:  # 如果是小写字母
            i_acsii = ord(i) - 32
        elif i in string.ascii_uppercase:  # 如果是大写字母
            i_acsii = ord(i) + 32
        res += chr(i_acsii)
    return res


def decrypt(str2):  # 解密过程：大写变小写，小写变大写，数字-1
    i_acsii, res = '', ''
    for i in str2:
        if i in string.digits:  # 如果是数字
            i_acsii = ord(i) - 1
        elif i in string.ascii_lowercase:  # 如果是小写字母
            i_acsii = ord(i) - 32
        elif i in string.ascii_uppercase:  # 如果是大写字母
            i_acsii = ord(i) + 32
        res += chr(i_acsii)
    return res


if __name__ == '__main__':
    # print(encryption('123qweQWE'))
    print(decrypt('234QWEqwe'))
