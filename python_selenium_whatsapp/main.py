from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('--allow-profiles-outside-user-dir')
options.add_argument('--enable-profile-shortcut-manager')
options.add_argument(r'user-data-dir='
                     r'D:\Users\Levashov\AllCode\Python\python_apps\WhatsAppAuto\drivers\chrome\selenium_profile')
options.add_argument('--profile-directory=Profile 1')
options.add_argument('--profiling-flush=n')
options.add_argument('--enable-aggressive-domstorage-flushing')

service = Service(r'D:\Users\Levashov\AllCode\Python\python_apps\WhatsAppAuto\drivers\chrome\chromedriver113.exe')
driver = webdriver.Chrome(service=service, options=options)


def main_func():
    try:
        wait = WebDriverWait(driver, 30)
        numbers = ["+79020365496", "+79633590005"]
        text = "Проверка 123"

        for number in numbers:
            url = f"https://web.whatsapp.com/send?phone={number}&text={text}"
            driver.get(url)
            wait.until(EC.element_to_be_clickable((By.XPATH, "//button[@data-testid='compose-btn-send']")))
            driver.find_element(By.XPATH, "//button[@data-testid='compose-btn-send']").click()
            sleep(5000)
            wait.until((EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='msg-dblcheck']"))))

        driver.close()
    except Exception as ex:
        print(ex)


main_func()
