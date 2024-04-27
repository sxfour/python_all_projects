import time, paramiko, threading

yellow = '\033[33;3m'
green = '\033[32;3m'
end = '\033[0m'
fail = '\x1b[31;3m'


def ssh(host, username, password, enable, command, max_bytes=60000, short_pause=1, long_pause=5, ):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname=host, username=username, password=password, look_for_keys=False, allow_agent=False,
                   timeout=2)
    with client.invoke_shell() as ssh:
        print(f'\n{yellow}[!]{end} [{host}] --> Waiting...')
        ssh.send('enable\n'), ssh.send(f'{enable}\n'), time.sleep(short_pause)
        ssh.send('terminal length 0\n'), time.sleep(short_pause), ssh.recv(max_bytes)
        results = dict()
        for command in execute_comm:
            ssh.send(f'{execute_comm}\n')
            ssh.settimeout(5)
            output = ''
            part = ssh.recv(max_bytes).decode('utf-8')
            output += part
            time.sleep(0.5)
        results[command] = output
        print(f'\t\t{results}')
        if results == {'whoami': "['whoami']\r\n\x1b[?2004l\r"}:
            stdin, stdout, srderr = client.exec_command('whoami')
            data = stdout.read() + srderr.read()
            client.close()
            print(f'\t\t\t{green}[+]{end} : {data}')


if __name__ == '__main__':
    libs = []
    for x in libs:
        execute_comm = ['whoami']
        try:
            ssh(x, 'root', 'toor', 'linux', execute_comm)
        except Exception as ex:
            print(f'\n{fail}[!]{end} [{x}] : {ex}')
