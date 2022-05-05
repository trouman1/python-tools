from bs4 import BeautifulSoup
import requests

resp = requests.get('https://www.cnblogs.com/')
# print(resp.text)
html = BeautifulSoup(resp.text, 'lxml')  # 初始化解析器

print(html.head.title.string)  # 查找页面元素(根据标签层次进行查找）(只能得到第一个)

# 查找页面元素的通用方法：
# 1、find_all：根据标签，属性，XPath等进行查找
# 2、select：CSS选择器，div, #id, .class

# links = html.findAll('a')  # 查找页面中的a标签
# for link in links:
#     print(link['href'])

# titles = html.findAll('a')  # 根据标签来查找
# for title in titles:
#     if title.string is None:
#         continue
#     print(title.string)

# titles = html.find_all(class_='post-item-title')  # 根据class属性来查找
# for title in titles:
#     print(title.string)

# titles = html.select('.post-item-title')  # CSS选择器
# for title in titles:
#     print(title.string)
