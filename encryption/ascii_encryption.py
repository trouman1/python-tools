# source = 'ILOVEYOU'
# for c in source:
#     new = ord(c)
#     new += 15
#     print(chr(new), end='')  # print默认是打印一行，结尾加换行，end=''意思是末尾不换行

source = 'X[^eTh^d'
for c in source:
    new = ord(c)
    new -= 15
    print(chr(new), end='')
