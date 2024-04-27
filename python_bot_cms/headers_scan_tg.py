from config import bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import requests

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('[ ! ] basic code v0.0.2\n'
                        '[ ! ] Hi, Im headers_scanner.\n'
                        '[ ! ] Sent me domain to scan\n'
                        '[ ! ] Example: https://google.com')


def get(site):
    global user_agent
    user_agent = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'}
    return requests.get(site, allow_redirects=False, headers=user_agent)


@dp.message_handler()
async def headers_scan(message: types.Message):
    global site
    try:
        site = message.text
        status = get(site)
    except requests.exceptions.ConnectionError as ex:
        await message.reply('[ ! ] Seems down...\n' + site)
    except requests.exceptions.MissingSchema as ex:
        await message.reply(f'[ ! ] Invalid URL: {site}')
    else:
        if status == 200 or status == 301 or status == 302:
            await message.reply(site + '[+] Seems online')
            redirect = requests.get(site, headers=user_agent)
            if len(redirect.history) > 0:
                if '301' in str(redirect.history[0]) or '302' in str(redirect.history[0]):
                    await message.reply('Ops, sites redirected me...' + redirect.url)
            elif 'meta http-equiv="REFRESH"' in redirect.text:
                await message.reply('[ ! ] Ops, site redirected me...')
            else:
                await message.reply('[ ! ] Site not appear to redirected...')
        for header in status.headers:
            try:
                print(header + ':' + status.headers[header])
                with open('headers.txt', 'a') as f:
                    f.write(f'\n' + header + ':' + status.headers[header]), f.close()
            except Exception as ex:
                await message.reply('[ ! ] Ops... ' + ex.message)

        robots_basic_check = requests.get(site + '/robots.txt', headers=user_agent)
        if robots_basic_check.status_code == 200:
            await message.reply('[+] Found robots.txt:\n' + f'{site}/robots.txt')
            print('\n[+] Found robots.txt:\n' + f'{site}/robots.txt')
        else:
            await message.reply('[-] Status page not found...')

    await message.reply_document(open('headers.txt', 'rb'))
    f = open('headers.txt', 'w')
    f.close()


if __name__ == '__main__':
    executor.start_polling(dp)
