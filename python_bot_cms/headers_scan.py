import requests


def get(site):
    global user_agent
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    return requests.get(site, allow_redirects=False, headers=user_agent)


def headers_scan():
    global site
    try:
        site = input('Set domain to scan\nExample: https://google.com\nSet:')
        status = get(site)
    except requests.exceptions.ConnectionError as ex:
        print(site + ' Seems down...')
    except requests.exceptions.MissingSchema as ex:
        print(f'Invalid URL: {site}')
    else:
        if status == 200 or status == 301 or status == 302:
            print(site + 'Seems online')
            redirect = requests.get(site, headers=user_agent)
            if len(redirect.history) > 0:
                if '301' in str(redirect.history[0]) or '302' in str(redirect.history[0]):
                    print('Ops, sites redirected me...' + redirect.url)
            elif 'meta http-equiv="REFRESH"' in redirect.text:
                print('Ops, site redirected me...')
            else:
                print('Site not appear to redirected...')
        print('Get HTTP headers...')
        for header in status.headers:
            try:
                print(header + ':' + status.headers[header])
            except Exception as ex:
                print('Ops... ' + ex.message)
    print('\nStarts robots.txt scan...')
    robots_check = requests.get(site + '/robots.txt', headers=user_agent)
    if robots_check.status_code == 200:
        print('robots.txt set on this site:\n' + f'{site}/robots.txt')
    else:
        print('Status page not found...')


if __name__ == '__main__':
    headers_scan()
