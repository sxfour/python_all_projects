from smb.SMBConnection import SMBConnection
import threading

green = '\033[32;3m'
yellow = '\033[33;3m'
fail = '\x1b[31;3m'
end = '\033[0m'


def smb_connect(ip, port, thr):
    # Connecting on 445 port with smbprotocol module
    try:
        username = 'User'
        password = 'User'
        domain = '.'
        client_name = 'Guest'
        if port == 445:
            is_direct_tcp = True
        else:
            is_direct_tcp = False
        # Options to connect SMB module
        conn = SMBConnection(username, password, client_name,
                             ip, domain, use_ntlm_v2=True,
                             is_direct_tcp=is_direct_tcp)
        smb_auth_successful = conn.connect(ip, port, timeout=10)
        if smb_auth_successful:
            all_shares = conn.listShares(timeout=10)
            # Append all results for host
            lib = {}
            for i in range(len(all_shares)):
                lib[i] = all_shares[i].name
            with open('output/allshares.txt', 'a') as f:
                f.write(f'{ip}:{lib}\n')
            print(f'{green}[+]{end} [SMB] [thr: {thr}] [{ip}]: '
                  f'{conn} Authentication successful: {yellow}[not checked] {lib}{end}')
        else:
            # Some errors may not display correctly, this is due to language conversion in folders
            print(f'{fail}[-]{end} [SMB] [thr: {thr}] [{ip}]: '
                  f'Authentication aborted, more:{yellow} Some errors may not display correctly, '
                  f'this is due to language conversion in folders{end}')
    except Exception as ex:
        print(f'{yellow}[!]{end} [SMB] [thr: {thr}] [{ip}]: Timeout from samba, more: {ex}')


if __name__ == '__main__':
    samba_lib = {}
    for ip in samba_lib:
        port = 445
        threading.Thread(target=smb_connect, args=(str(ip), port, threading.active_count())).start()
