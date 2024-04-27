from html2image import Html2Image
from subprocess import Popen, PIPE
from postgresql import AddHosts
import requests

# ASCII color codes
green = '\033[32;3m'
yellow = '\033[33;3m'
fail = '\x1b[31;3m'
end = '\033[0m'


def headers_scan(site):
    siteHttp = str('http://' + site)
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    hti = Html2Image(custom_flags=["--headless", "--disable-gpu", "--no-sandbox"], output_path='png/')
    hti.size = (1280, 720)
    try:
        status = requests.get(siteHttp, allow_redirects=True, headers=user_agent, timeout=2)
        statusCode = status.status_code
        if statusCode == 200 or statusCode == 301 or statusCode == 302:
            dataHeader = str()

            print(f'\n{green}{siteHttp} - target seems online {end}')

            for header in status.headers:
                try:
                    dataHeader += header + ':' + status.headers[header].replace("'", "")
                    dataHeader += '/'

                    print(header + ':' + status.headers[header])
                except Exception as ex:
                    print('Ops... ', ex)

            hti.screenshot(url=siteHttp, save_as=f'{site}.png')

            AddHosts().appendHTTPHostPostgreSQL('HTTPhosts', site, '80', dataHeader, f'{site}.png')

    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as ex:
        print(f'{yellow}{site} Seems down... {ex}{end}')

    except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as ex:
        print(f'{fail}Invalid URL: {siteHttp} {ex}{end}')


def get_pipe():
    args = ['masscan', '92.0.0.0-94.0.0.0', '-p', '80', '--rate', '25', '--connection-timeout', '10']
    process = Popen(args, stdout=PIPE)

    for line in process.stdout:
        host = line.decode('cp866').split()
        try:
            headers_scan(str(host[5]))
        except Exception as ex:
            print(f'{ex}')

    data, error = process.communicate()

    print(error)

    return data.decode(encoding='cp866')


def startPipe():
    print(get_pipe())
    input()


if __name__ == '__main__':
    startPipe()
