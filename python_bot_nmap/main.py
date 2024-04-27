from selenium import webdriver
from selenium.webdriver.common.by import By
import time

options = webdriver.ChromeOptions()
options.headless = True
driver = webdriver.Chrome(options=options)


def selen_func():
    try:
        driver.get('https://hackertarget.com/nmap-online-port-scanner/')
        get_ip = driver.find_element(By.NAME, 'theinput')
        get_ip.send_keys(input('Set host: '))
        print('Sending command...')
        driver.find_element(By.ID, 'clickform').click()
        time.sleep(5)

        scanIp = driver.find_element(By.ID, 'formResponse')
        print(f'{scanIp.text}')
    except Exception as ex:
        print(ex)


selen_func()
