from smb.SMBConnection import SMBConnection


def smb_connect(ip, port, username, password, client, domain, service_name, path):
    try:
        conn = SMBConnection(username, password, client, ip, domain, use_ntlm_v2=True, is_direct_tcp=True)
        conn.connect(ip, port, timeout=30)

        a_ = conn.listPath('Buh', '/', search=65591, pattern='*', timeout=30)
        lib_dir = list()
        for files in a_:
            lib_dir.append(files.filename)
        print(lib_dir)

        # s_ = conn.getSecurity(service_name=service_name, path=path, timeout=30)
        # sall_ = list([s_.owner, s_.group, s_.dacl, s_.sacl, s_.flags])
        # print(f'\nSecurity parameters --->\n{sall_}\n')

        # g_ = conn.getAttributes(service_name=service_name, path=path, timeout=30)
        # gall_ = list([g_.filename, g_.file_attributes, g_.file_size, g_.create_time, g_.last_access_time])
        # print(f'Attributes --->\n{gall_}\n')
        conn.close()
    except Exception as ex:
        print(ex)


smb_connect(ip='78.138.127.102', port=445, username='User', password='User', client='User', domain='.', service_name='Buh', path='RECOVERY.hta')
