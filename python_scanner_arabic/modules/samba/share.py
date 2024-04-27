import threading
from smb.SMBConnection import SMBConnection, OperationFailure, NotReadyError

# ANSI color code https://ansi.gabebanks.net/ and list ips
green = '\033[32;3m'
yellow = '\033[33;3m'
fail = '\x1b[31;3m'
end = '\033[0m'


def smb_connect(ip, port, thr):
    try:
        username = 'User'
        password = 'User'
        client = 'Guest'
        domain = '.'
        # Basic options to connect Samba
        conn = SMBConnection(username, password, client, ip, domain, use_ntlm_v2=True, is_direct_tcp=True)
        conn.connect(ip, port, timeout=10)
        shares = conn.listShares(timeout=10)
        lib_dir = []
        for i in range(len(shares)):
            lib_dir.append(shares[i].name)
        for x in lib_dir:
            auth = dict()
            try:
                # Connection to path with SMB module
                conn.listPath(x, '/')
                auth['open'] = x
                with open('output/openshares.txt', 'a') as f:
                    f.write(f'{ip}:{auth}\n')
                print(f'{green}[+]{end} [SMB Share] [thr: {thr}] [{ip}]: Authentication successful: {auth}')
            except OperationFailure:
                auth['close'] = x
                print(f'{fail}[-]{end} [SMB Share] [thr: {thr}] [{ip}]: Authentication error: {auth}')
    except TimeoutError as ex:
        print(f'{yellow}[!]{end} [SMB Share] [thr: {thr}] [{ip}]: Timeout from server, more: {ex}')
    except OperationFailure:
        print(f'{yellow}[!]{end} [SMB Share] [thr: {thr}] [{ip}]: Connection active, but need administrator privilege')
    except NotReadyError:
        print(f'{yellow}[T]{end} [SMB Share] [thr: {thr}] [{ip}]:'
              f' Sometimes share opened, this mistake tied to language check share!')


if __name__ == '__main__':
    samba_lib = {}
    for x in samba_lib:
        port = 445
        threading.Thread(target=smb_connect, args=(str(x), port, threading.active_count())).start()
