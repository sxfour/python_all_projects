# 195.208.132.196

import shodan
import requests

SHODAN_API_KEY = "Pe3YdGks3juloSfWPRy3RK0OSqXdY7Jt"
api = shodan.Shodan(SHODAN_API_KEY)

target = '212.26.239.159'

dnsResolve = 'https://api.shodan.io/dns/resolve?hostnames=' + target + '&key=' + SHODAN_API_KEY

try:
    # First we need to resolve our targets domain to an IP
    resolved = requests.get(dnsResolve)
    hostIP = resolved.json()[target]

    # Then we need to do a Shodan search on that IP
    host = api.host(hostIP)
    print("IP: %s" % host['ip_str'])
    print("Organization: %s" % host.get('org', 'n/a'))
    print("Operating System: %s" % host.get('os', 'n/a'))

    # Print all banners
    for item in host['data']:
        print("Port: %s" % item['port'])
        print("Banner: %s" % item['data'])

    # Print vuln information
    for item in host['vulns']:
        CVE = item.replace('!','')
        print('Vulns: %s' % item)
        exploits = api.exploits.search(CVE)
        for item in exploits['matches']:
            if item.get('cve')[0] == CVE:
                print(item.get('description'))
except:
    print('An error occured')