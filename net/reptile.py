import random
import re
import requests


def random_articlenum(homepage, trailerpage):  # 随机获取5篇文章的文章号 homepage：输入起始页，trailerpage：输入结束页
    articlenum = []
    randomartic = []
    for i in range(homepage, trailerpage + 1):
        resp = requests.get(f'https://www.woniuxy.com/note/page-{i}').text
        re1 = '<div class="title">(.+?)>'
        list1 = re.findall(re1, resp)
        for l in list1:
            articlenum.append(l.split('/')[2][0:3])
    for n in range(5):
        randomartic.append(random.choice(articlenum))
    return randomartic
    # print(randomartic)


def reptile_title(homepage, trailerpage):  # homepage：输入起始页，trailerpage：输入结束页
    re1 = '<div class="title">(.+?)<'
    for i in range(homepage, trailerpage + 1):
        resp = requests.get(f"https://www.woniuxy.com/note/page-{i}").text
        list1 = re.findall(re1, resp)
        # print(list1)
        for l in list1:
            title = l.split('>')[1]
            print(title)


def reptile_img():  # 随机下载10——20页的5篇文章的所有img
    for i in random_articlenum(10, 20):
        resp = requests.get(f"https://www.woniuxy.com/note/{i}").text
        re1 = '<img src="(.+?)"'
        list1 = re.findall(re1, resp)
        for img in list1:
            if img.startswith('/'):
                img = f"https://www.woniuxy.com/note/{i}" + img
            resp = requests.get(img)
            filename = img.split('/')[-1]
            with open('../temp/reptile/' + filename, mode='wb') as file:
                file.write(resp.content)


if __name__ == '__main__':
    # reptile_title(1, 20)
    # random_articlenum(1, 2)
    reptile_img()
