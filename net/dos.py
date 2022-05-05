import requests
import threading


def login():
    url = 'http://192.168.0.105:8080/user/login'
    data = {"username": "1", "password": "1", "verifycode": "0000"}
    resp = requests.post(url=url, data=data)
    print(resp.text)
    login()


if __name__ == '__main__':
    for i in range(100):
        t = threading.Thread(target=login)
        t.start()
