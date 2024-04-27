from config import bot_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)

bot = Bot(token=bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.reply('Sent host or domain to scan\nExample: 8.8.8.8 ')


@dp.message_handler()
async def get_info(message: types.Message):
    try:
        driver.get('https://hackertarget.com/nmap-online-port-scanner/')
        get_ip = driver.find_element(By.NAME, 'theinput')
        get_ip.send_keys(f'{message.text}')

        await message.reply('Sending command...')
        driver.find_element(By.ID, 'clickform').click()
        time.sleep(5)

        scanIp = driver.find_element(By.ID, 'formResponse')
        await message.reply(f'{scanIp.text}')
    except Exception as ex:
        print(ex)


if __name__ == '__main__':
    executor.start_polling(dp)
