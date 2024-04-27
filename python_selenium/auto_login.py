from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# """Rename user-agent and off webdriver"""
# options = webdriver.ChromeOptions()
# options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; WOW64; rv:45.0) Gecko/20100101 Firefox/45.0 ')
# options.add_argument('--disable-blink-features=AutomationController')
# options.headless = True
# driver = webdriver.Chrome(
#     executable_path=r'C:\Users\Levashov\PycharmProjects\pythonProject\my_modules\SeleniumChrome\chromedriver(70.0.3538.16).exe',
#     options=options
# )

driver = webdriver.Chrome()

try:
    driver.get('https://vk.com')
    assert 'Добро пожаловать | ВКонтакте' in driver.title
    get_login = driver.find_element(By.ID, 'index_email')
    get_login.send_keys('+79005553535')
    time.sleep(5)

    driver.find_element(By.CLASS_NAME, 'VkIdForm__signInButton').click()
    time.sleep(5)

    get_password = driver.find_element(By.NAME, 'password')
    get_password.send_keys('1234567890')
    driver.find_element(By.CLASS_NAME, 'vkc__Password__ViewIcon').click(), time.sleep(2)
    get_password.send_keys(Keys.ENTER)
    time.sleep(10)
except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()