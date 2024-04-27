from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import datetime

# Headers and User-agent settings, if you need to see browser gui, set options.headless = False
options = webdriver.ChromeOptions()
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0')
options.add_argument('--disable-blink-features=AutomationController')
options.headless = False
driver = webdriver.Chrome(
    executable_path=r'C:\Users\Levashov\PycharmProjects\pythonProject\my_modules\SeleniumChrome\chromedriver.exe',
    options=options
)


def avito_func():
    try:
        driver.get('https://www.avito.ru/monchegorsk/vakansii?cd=1&s=104')
        items = driver.find_elements(By.XPATH, '//div[@data-marker="item"]')
        items[0].click()
        driver.implicitly_wait(10)

        driver.switch_to.window(driver.window_handles[0])
        driver.implicitly_wait(10)
        print(f'Url:{driver.current_url}')
    except Exception as ex:
        print(ex)
    finally:
        driver.close()
        driver.quit()


avito_func()
