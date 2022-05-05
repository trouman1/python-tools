import socket


def get_port():
    common = [7, 21, 22, 23, 25, 43, 53, 67, 68, 69, 79, 80, 81, 88, 109, 110, 113, 119, 123, 135, 135, 137, 138, 139,
              143, 161, 162, 179, 194, 220, 389, 443, 445, 465, 513, 520, 520, 546, 547, 554, 563, 631, 636, 991, 993,
              995, 1080, 1194, 1433, 1434, 1494, 1521, 1701, 1723, 1755, 1812, 1813, 1863, 3269, 3306, 3307, 3389, 3544,
              4369, 5060, 5061, 5355, 5432, 5671, 5672, 6379, 7001, 8080, 8081, 8088, 8443, 8883, 8888, 9443, 9988,
              9988, 15672, 50389, 50636, 61613, 61614]
    for port in common:
        try:
            s = socket.socket()
            s.settimeout(0.5)
            s.connect(('192.168.0.109', port))
            print(port)
            s.close()
        except:
            pass


if __name__ == '__main__':
    get_port()