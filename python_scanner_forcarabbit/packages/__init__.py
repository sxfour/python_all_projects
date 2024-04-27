import socket


class ForceWorker:
    def __init__(self, host, port):
        self.host = host
        self.port = port

        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.s.settimeout(0.5)

        self.startSocket()

    def startSocket(self):
        try:
            self.s.connect((self.host, self.port))
            self.s.close()

            print(self.host, self.port)

        except Exception as ex:
            pass
