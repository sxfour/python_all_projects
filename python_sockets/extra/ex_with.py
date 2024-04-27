import socket

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.bind(('127.0.0.1', 8888))
    print('8888 is bind')

    while True:
        result = sock.recv(1024)
        print('Message', result.decode('utf-8'))