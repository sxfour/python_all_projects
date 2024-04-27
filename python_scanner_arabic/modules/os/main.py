from requests import exceptions
from bs4 import BeautifulSoup
import requests, datetime, nmap

# Using port_scan module with portscan
nma = nmap.PortScannerAsync()

green = '\033[32;3m'
yellow = '\033[33;3m'
fail = '\x1b[31;3m'
end = '\033[0m'


# Scanning geolocation and etc, with api module
def geo(host):
    url = 'http://ip-api.com/batch'
    try:
        # API settings to get response message from server (More API settings on this site
        # http://ip-api.com/batch
        settings = [{"query": f"{host}",
                     "fields": "city,country,countryCode,query,lat,lon,isp,org,asname",
                     "lang": "us"}]
        response = requests.post(url, json=settings)
        if response.status_code == 200:
            with open('output/geo.txt', 'a') as f:
                f.write(f'{response.text[1:-1]}\n')
            print(f'{green}[+]{end} [G] [{host}]: {response.text[1:-1]}')
        if response.status_code == 429:
            print(f'{yellow}[!]{end} [G] [{host}]: Timeout server')
    except exceptions.ConnectionError:
        print(f'{fail}[!]{end} [G] [{host}]: Connection aborted')
    except IndexError as ex:
        print(f'{yellow}[!]{end} [G] [Count: {host}]:', ex)


# Checking title (using requests and bs4) on all ip list, its so basic and stupid code < but he works...
def headers(host):
    user_agent = {'User-Agent': 'Mozilla/5.0'
                                ' (Windows NT 10.0; '
                                'WOW64) AppleWebKit/537.36'
                                ' (KHTML, like Gecko)'}
    try:
        url = requests.get(url=f'http://{host}/', allow_redirects=False, headers=user_agent)
    except requests.exceptions.ConnectionError:
        print(f'{yellow}[!]{end} [H] [{host}]: Seems down')
    else:
        soup = BeautifulSoup(url.text, 'html.fstec')
        print(f'{yellow}[!]{end} [H] [{host}]: {soup.find_all("title")} {url.headers}')


# Two func, first scanner port_scan module, last save output json files without sortkeys and indent
def nmap_scan(host):
    try:
        nma.scan(hosts=host, arguments='-F -O', callback=nmap_result)
        while nma.still_scanning():
            print(f'{yellow}[!]{end} Scanning at '
                  f'{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}')
            nma.wait(25)
    except Exception as ex:
        print(ex)


def nmap_result(host, scan_result):
    try:
        # Example for json tabs: json.dumps(scan_result, sort_keys=True, indent=4)
        os_main_info = scan_result['scan'][f'{host}']['osmatch']
        with open('output/osnmap.txt', 'a') as f:
            f.write(f'{os_main_info}\n')
        print(f'{green}[+]{end} [N] [{host}]: {os_main_info}\n')
    except Exception as ex:
        print(f'{yellow}[!]{end} [N] [{ex}]: Timeout\n')


if __name__ == '__main__':
    hosts_lib = {'192.168.0.110'}
    for ip in hosts_lib:
        geo(ip)
        headers(ip)
        nmap_scan(ip)
