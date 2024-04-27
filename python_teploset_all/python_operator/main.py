from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, NoSuchWindowException
from info import p_2, main_lib
import datetime
import keyboard
import time

# print('[!] Waiting 20 seconds to start...')
# time.sleep(20)

# Запуск браузера + опции запуска, режим with gui, полноэкранный режим.
options = webdriver.ChromeOptions()
options.headless = False
options.add_argument('--start-fullscreen')
driver = webdriver.Chrome(options=options, executable_path='chromedriver.exe')


# Функция для входа в screener c помощью selenium.
def main():
    try:
        print('\n[+] Starting service...')
        driver.get(main_lib[1])
        # Поиск элемента для входа с помощью XPath.
        auth_form = driver.find_element(By.CLASS_NAME, main_lib[3])
        auth_form.send_keys(p_2)
        driver.find_element(By.CLASS_NAME, main_lib[2]).click()
        time.sleep(6)
        # Выбор монитора и скрытие панели с помощью XPath.
        driver.find_element(By.XPATH, "//label[@for='monitor-1-2']").click()
        driver.find_element(By.XPATH, "//div[@class='panel__realsize panel__single "
                                      "/ js-panel-realsize js-tooltip']").click()
        driver.find_element(By.XPATH, "/html/body/div[5]/div[1]/div[2]/div[1]").click()
    except Exception as ex:
        print(ex)


# Функция с циклом, для проверки наличия открытого соединения в браузере.
# Если XPath обнаружен на странице (XPath будет соответствовать ошибочному окну) выполняется переподключение или выход.
def out():
    param = []
    while param != bool:
        try:
            param = driver.find_element(By.XPATH, "//div[@class='register__title']")
            print(f'\n[+] Xpath founded at     [{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}]'
                  f'\t[Session closed]')
            print('[!] Restarting service...')
            driver.get(main_lib[1])
            auth_form = driver.find_element(By.CLASS_NAME, main_lib[3])
            auth_form.send_keys(p_2)
            driver.find_element(By.CLASS_NAME, main_lib[2]).click()
            time.sleep(6)
            driver.find_element(By.XPATH, "//label[@for='monitor-1-1']").click()
            driver.find_element(By.XPATH, "//div[@class='video-box / js-video-box']").click()
            time.sleep(12)
        except NoSuchElementException:
            print(f'[-] XPath not founded at [{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}]'
                  f'\t[Session opened]')
            time.sleep(12)
        except NoSuchWindowException:
            print(f'\n[!] Window are closed at [{datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S")}]'
                  f'\t[Session closed]')
            print('[!] Stopping service...')
            keyboard.send('alt+f4')
            exit()


if __name__ == '__main__':
    main()
    out()
    driver.close()
    driver.quit()
