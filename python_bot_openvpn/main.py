from info import p_2
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
import datetime

bot = Bot(token=p_2)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def str_cmd(message: types.Message):
    print(f'[+] Starting bot at \t[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]')
    await message.reply('[ ! ] Hi, Im OpenVPN bot!\n'
                        '[ ! ] OS: Debian 11 (ENG)\n'
                        '[ ! ] IP: 195.133.1.177\n'
                        '[ ! ] Config: 1x2.2ГГц, 0.5Гб RAM, 1IP\n'
                        '[ ! ] Use my config and safe traffic\n'
                        '[ ! ] Connect for me, with OpenVPN\n'
                        '[ ! ] Download OpenVPN android, /apk\n'
                        )


@dp.message_handler(commands=['configuration'])
async def conf_cmd(message: types.Message):
    print(f'[+] Reply config at \t[{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}]')
    await message.reply_document(open('homevpn.ovpn', 'rb'))
    await message.reply_document(open('homepc.ovpn', 'rb'))


@dp.message_handler(commands=['other'])
async def other_cmd(message: types.Message):
    await message.reply_document(open('andr.ovpn', 'rb'))


@dp.message_handler(commands=['apk'])
async def conf_cmd(message: types.Message):
    await message.reply('https://play.google.com/store/apps/details?id=net.openvpn.openvpn&hl=en&gl=US')


@dp.message_handler()
async def oth_msg(message: types.Message):
    await message.reply('[ ! ] Error command!\n'
                        '[ ! ] Print /start for more info')


if __name__ == '__main__':
    executor.start_polling(dp)
