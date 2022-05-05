import math
import time


def get_prime(n, m):  # 获取质数，区间为[n,m]
    for i in range(n, m + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print(i)


def is_prime(n):  # 求质数优化：减少循环次数
    maxn = int(math.sqrt(n)) + 1  # 任何一个数，其因子只需要找小于其开根号的整数即可，
    for i in range(2, maxn):
        if n % i == 0:
            return False
    return True


def prime_pq(n):  # 给定一个数，求其乘积因子，并确保一定是质数
    for p in range(1, n):
        for q in range(1, n):
            if p * q == n and is_prime(p) and is_prime(q):  # 如果找到因子且两个因子均为质数，则可以直接得出结论，不需要继续循环
                return f"{p}*{n // p}={n}"


def prime_pq_v2(n):  # 算法优化：p和q的循环次数减半
    for p in range(1, n // 2 + 1):
        for q in range(1, n // 2 + 1):
            if p * q == n and is_prime(p) and is_prime(q):
                return f"{p}*{n // p}={n}"


def prime_pq_v3(n):  # dgy的算法
    maxn = int(math.sqrt(n)) + 1
    for p in range(2, maxn):  # 只要得出其中一个因子，另外一个因子就可以算出来
        if is_prime(p) and n % p == 0 and is_prime(n // p):
            return f"{p}*{n // p}={n}"


if __name__ == '__main__':
    start = time.time()

    # print(is_prime(997))
    # get_prime(9000000, 10000000)

    # 641*643=412163
    print(prime_pq(412163))  # 10.006611824035645s
    # print(prime_pq_v2(412163))  # 5.010601043701172s
    # print(prime_pq_v3(412163))  # 0.0010006427764892578s

    end = time.time()
    print(end - start)

# 已知两个质数的乘积为 N ，对应整数为：
# 1230186684530117755130494958384962720772853569595334792197322452151726400507263657518745202199786469389956474942774063845925192557326303453731548268507917026122142913461670429214311602221240479274737794080665351419597459856902143413
# 计算两个质数因子 P 和 Q，结果如下：
# P = 33478071698956898786044169848212690817704794983713768568912431388982883793878002287614711652531743087737814467999489
# Q = 36746043666799590428244633799627952632279158164343087642676032283815739666511279233373417143396810270092798736308917
