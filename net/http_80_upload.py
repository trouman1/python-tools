import requests


def upload_post():  # 通过使用session对象来发送请求，可以一直维持状态
    session = requests.session()
    login_url = 'http://192.168.0.117:8080/user/login'  # 用fiddle得到
    login_data = {'username': '1', 'password': '1', 'verifycode': '0000'}  # 用fiddle得到
    session.post(url=login_url, data=login_data)
    upload_url = 'http://192.168.0.117:8080/goods/upload'
    for i in range(1000):
        i += 1
        data = {'batchname': f'{i}'}
        file = {'batchfile': open(r'E:\PycharmProjects\pythonProject\learn\temp\SaleList-20171020-Test.xls', 'rb')}
        upload_resp = session.post(url=upload_url, data=data, files=file)
        print(upload_resp.text)


if __name__ == '__main__':
    upload_post()
