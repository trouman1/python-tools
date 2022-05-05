import socket
import threading


def get_port(i):
    for port in i:
        s = socket.socket()
        s.settimeout(1)
        try:
            s.connect(('localhost', port))
            print(port)
            s.close()
        except:
            pass


if __name__ == '__main__':
    port_total = []
    for t in range(1, 65536):
        port_total.append(t)
    port_list = []
    for l in range(0, 65536, 500):  # 看需要分多少组
        port_list.append(port_total[l:l + 500])
    for ports in port_list:
        threading.Thread(target=get_port, args=(ports,)).start()
