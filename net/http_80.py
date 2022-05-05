import requests
import re


def get():  # requests下还有很多模式！
    res = requests.get('https://woniuxy.com/sc/toNote/7003-497')  # 用get的方式获取
    res.encoding = 'utf-8'  # 设置编码格式
    print(res.text)  # 打印响应正文


def login_post():
    url = 'http://192.168.0.117:8080/user/login'  # 用fiddle得到
    data = {'username': '1', 'password': '1', 'verifycode': '0000'}  # 用fiddle得到
    resp = requests.post(url=url, data=data)
    print(resp.text)
    # print(resp.headers)  # 打印响应头
    #
    list1 = re.findall('JSESSIONID=(.+?);', resp.headers['Set-Cookie'])
    return list1[0]  # add_post1()需要的返回值
    #
    # return resp.cookies  # add_post2()需要的返回值
    #


def add_post1():  # 用提取的方式来获取cookie
    cookie = {'JSESSIONID': login_post()}
    url = 'http://192.168.150.176:8080/WoniuSales1.4/customer/add'
    data = {'customername': 'root1', 'customerphone': '12341666111', 'childsex': '男', 'childdate': '2022-02-25',
            'creditkids': '9999', 'creditcloth': '9999'}
    resp = requests.post(url=url, data=data, cookies=cookie)
    print(resp.text)
    # print(resp.headers)  # 打印响应头
    # print(cookie)


def add_post2():  # 直接从相应中获取cookie
    cookie = login_post()
    url = 'http://192.168.150.176:8080/WoniuSales1.4/customer/add'
    data = {'customername': 'root2', 'customerphone': '122241111', 'childsex': '男', 'childdate': '2022-02-25',
            'creditkids': '9999', 'creditcloth': '9999'}
    resp = requests.post(url=url, data=data, cookies=cookie)
    print(resp.text)


def add_post3():  # 通过使用session对象来发送请求，可以一直维持状态
    session = requests.session()
    login_url = 'http://192.168.0.117:8080/user/login'  # 用fiddle得到
    login_data = {'username': '1', 'password': '1', 'verifycode': '0000'}  # 用fiddle得到
    session.post(url=login_url, data=login_data)
    add_url = 'http://192.168.0.117:8080/customer/add'
    for i in range(100):
        i += 1
        phone = f"134{i}"
        add_data = {'customername': 'root1', 'customerphone': phone, 'childsex': '男', 'childdate': '2022-02-25',
                    'creditkids': '9999', 'creditcloth': '9999'}
        add_resp = session.post(url=add_url, data=add_data)
        print(add_resp.text)


if __name__ == '__main__':
    # get()
    # login_post()
    # add_post1()
    # add_post2()
    add_post3()
