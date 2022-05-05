import socket


def get_subdomain(domain):
    with open('../dict/subdomain/subdomain_top160k.txt') as file:
        domain_list = file.readlines()
    for subdomain in domain_list:
        try:
            ip = socket.gethostbyname(f"{subdomain.strip()}.{domain}")  # gethostbyname=返回的是主机名的IPv4的地址格式
            print(f"{subdomain.strip()}.{domain}, {ip}")
        except socket.gaierror:
            pass


if __name__ == '__main__':
    get_subdomain('woniuxy.com')
