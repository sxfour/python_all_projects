import threading, socket
from netaddr import *
from pyvis.network import Network

green = '\033[32;3m'
yellow = '\033[33;3m'
fail = '\x1b[31;3m'
end = '\033[0m'


def basic_scan(port, host):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # If you need to faster, set 0.5 seconds timeout sockets
    sock.settimeout(0.5)
    try:
        sock.connect((host, port)), print(f'{host}:{port}')
        sock.close()
        with open('output/ip_list.txt', 'a') as f:
            f.write(f'{host}:{port}\n')
            #f.write(f'{host} ')
    except Exception as ex:
        pass
        # print(f'{host}:{ex}')


def network_map(source, weights):
    # Creating a network map with pyvis module, all scanned hosts
    net = Network(height='1000px', width='1920px', bgcolor='#222222', font_color='white', filter_menu=True)
    net.barnes_hut()
    print(f'\n{yellow}[NETWORK MAP]{end} pyvis visualisation with js ---> {green}Starting...{end}')
    with open('output/ip_list.txt', 'r') as f:
        hosts = f.read().rstrip('\n')
        print(f'{green}[+]{end} Adding nodes...')
        for key in hosts.splitlines():
            hosts = list()
            hosts.append(key)
            edge_data = zip(hosts, source, weights)
            for e in edge_data:
                src = e[0]
                dst = e[1]
                w = e[2]
                net.add_node(src, src, title='Hi!\n This is test message.', color='#14b0fe')
                net.add_node(dst, dst, title='Locale server', color='#fead0b')
                net.add_edge(src, dst, value=w)
    net.get_adj_list()
    # Some options auto set on js settings, for exp ---> net.show_buttons(['physics']) and copy options code to
    # net.set_options('''OPTIONS CODE''')
    # net.set_options()
    net.show_buttons(['physics'])
    net.save_graph('test.html')
    print(f'{green}[+]{end} Saved from: test.html')


if __name__ == '__main__':
    # ips, ipe = '178.60.221.0-178.65.221.255'.split('-')
    # ipr = IPRange(ips, ipe)
    # port = 445
    # for ip in ipr:
    #     threading.Thread(target=basic_scan, args=(port, str(ip))).start()
    # Source = your locale name or locale host
    network_map(['locale'], ['10'])
