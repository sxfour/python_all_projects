from smb.SMBConnection import SMBConnection, OperationFailure, ProtocolError, NotConnectedError, SMBTimeout
import logging


def dumps_dir(ip, port, username, password, client, domain):
    try:
        conn = SMBConnection(username, password, client, ip, domain, use_ntlm_v2=True, is_direct_tcp=True)
        conn.connect(ip, port, timeout=30)
        shares = conn.listShares(timeout=30)
        lib_dir = list()
        for i in range(len(shares)):
            lib_dir.append(shares[i].name)
        for x in lib_dir:
            try:
                conn.listPath(x, '/')

                a_ = conn.listPath(x, '/', search=65591, pattern='*', timeout=30)
                lib_dir_v2 = list()
                for files in a_:
                    lib_dir_v2.append(files.filename)
                # with open('output/dump_dirs.txt', 'a') as f:
                #     f.write(f'[{ip}]:[{x}]:{lib_dir_v2[2:]}\n')
                print(ip, x, lib_dir_v2[2:])
            except OperationFailure:
                print(f'Closed share {x} on {ip}')
            except (ProtocolError, NotConnectedError, SMBTimeout):
                logging.exception(f'Two step error, please check {ip}')
    except TimeoutError as ex:
        print(f'Timeout: {ip}, {ex}')
    except (ProtocolError, NotConnectedError, SMBTimeout):
        logging.exception(f'First step error, please check {ip}')


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, filename='dump_smb.log', filemode='w',
                        format='%(asctime)s %(levelname)s %(message)s')
    logging.info('Start scanning...')
    samba_lib = {}
    for ip in samba_lib:
        dumps_dir(ip=ip, port=445, username='User', password='User', client='User', domain='.')
