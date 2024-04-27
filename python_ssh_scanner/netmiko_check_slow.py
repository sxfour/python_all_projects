from netmiko import ConnectHandler


def send_show_command(device, commands):
    try:
        with ConnectHandler(device_type='linux', ip=device, username='root', password='MYR9Yf9GOy') as ssh:
            for command in commands:
                output = ssh.send_command(command)
                print(f'[+] Authentication success : {device} {output}')
    except Exception:
        print(f'[!] Authentication failed : {device}')


if __name__ == '__main__':
    ssh_lib = ['195.133.1.177', '80.24.6.6', '80.23.147.123', '80.23.101.218', ]
    for x in ssh_lib:
        send_show_command(x, ['ls'])
