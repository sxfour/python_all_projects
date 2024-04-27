from rich.console import Console
from rich.table import Table
import nmap


class ScannerNmap:
    def __init__(self, host, port, width):
        self.console = Console(width=width)
        self.table = Table(title=host)
        self.nmap = nmap.PortScanner()
        self.host = host
        self.port = port

    def rollingScan(self):
        print('Starting...')
        self.nmap.scan(self.host, self.port)
        for host in self.nmap.all_hosts():
            for protocol in self.nmap[host].all_protocols():
                port_ = self.nmap[host][protocol].keys()
                sorted(port_)
                for port in port_:
                    # print(self.nmap[host][protocol][port])
                    self.table.add_row(str(port),
                                       self.nmap[host][protocol][port]['state'], self.nmap[host][protocol][port]['name'],
                                       self.nmap[host][protocol][port]['product'], self.nmap[host][protocol][port]['version'],
                                       self.nmap[host][protocol][port]['reason'], self.nmap[host][protocol][port]['cpe'], )
        self.console.print(self.table)
        print('advanced : %s\nversion : %s' % (self.nmap.scanstats(), self.nmap.nmap_version()))

    def createTable(self, justify):
        columns = [
            'port', 'state', 'name', 'service', 'version', 'reason', 'cpe', 'fstec'
        ]
        for key in columns:
            self.table.add_column(key, no_wrap=True, justify=justify)
        return self.table


start1 = ScannerNmap(host='192.168.0.1', port='22-443', width=1920)
start1.createTable(justify='right')
start1.rollingScan()
