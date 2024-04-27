from rich.console import Console
from rich.table import Table

import nmap


class ScannerNmap:

    def __init__(self, host, port, width):
        self.host = host
        self.port = port

        self.nmap = nmap.PortScanner()
        self.version = self.nmap.nmap_version()

        self.console = Console(width=width)
        self.table = Table(title='\nHost : %s \tNmap version : %s \tPorts : %s' % (host, self.version, self.port))

    def rollingScan(self):
        # print('\nNmap version : %s.%s' % self.port_scan.nmap_version())
        self.nmap.scan(self.host, self.port)

        for host in self.nmap.all_hosts():
            for protocol in self.nmap[host].all_protocols():

                port_ = self.nmap[host][protocol].keys()
                sorted(port_)

                for port in port_:
                    # print(self.port_scan[host][protocol][port])
                    self.table.add_row(str(port),
                                       self.nmap[host][protocol][port]['state'],
                                       self.nmap[host][protocol][port]['name'],
                                       self.nmap[host][protocol][port]['product'],
                                       self.nmap[host][protocol][port]['version'],
                                       self.nmap[host][protocol][port]['reason'],
                                       self.nmap[host][protocol][port]['cpe'], )

        self.console.print(self.table)
        # print('advanced : %s\nversion : %s' % (self.port_scan.scanstats(), self.port_scan.nmap_version()))

    def createTable_nmap(self, justify, columns):
        for key in columns:
            self.table.add_column(key, no_wrap=True, justify=justify)
        return self.table
