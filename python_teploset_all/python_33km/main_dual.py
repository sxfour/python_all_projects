# Tested on Python 3.9, Windows 10 64bit

from selenium.common.exceptions import (
    NoSuchWindowException,
    InvalidSessionIdException,
    WebDriverException,
)
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from settings import decrypted
from selenium import webdriver
from time import sleep


class Browser:

    def __init__(self, http_url, key, options, path):
        self.key = key
        self.url = http_url
        self.sleep = sleep
        self.options = options
        self.html = path

        # Window open with chrome driver.
        self.driver = webdriver.Chrome(service=Service("drivers/chrome/chromedriver.exe"), options=self.options)
        self.driver.set_window_size(width=3840, height=1080)
        self.driver.set_window_position(x=0, y=0)

        self.driver.get(self.html[0])
        self.sleep(5)

        self.driver.get(self.url[0])

    def startWindows(self):
        try:
            self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(self.key)
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(self.key)
            self.driver.find_element(By.XPATH, "//button[@class='button']").click()
            self.sleep(5)
            self.driver.execute_script(f"window.open('{self.url[1]}')")

            CDWindow_0 = self.driver.window_handles[0]
            CDWindow_1 = self.driver.window_handles[1]

            self.sleep(5)
            self.driver.switch_to.window(CDWindow_0)
            self.driver.close()

            self.driver.switch_to.window(CDWindow_1)

        except Exception as ex:
            print(ex)

    def freshWindows(self, errorMessages):
        try:
            index = 0
            while self.driver.current_url != 0:
                if (errorMessages[0] == self.driver.current_url
                        or errorMessages[1] == self.driver.current_url):
                    print("Error link : %r" % self.driver.current_url)
                    self.driver.close()
                    self.driver.quit()

                    Browser.startBrowser()
                    break
                else:
                    index += 1
                    print(f"\n[count: {index}] Opened link : %r" % self.driver.current_url)

                    # Reload page.
                    self.driver.refresh()
                    self.driver.execute_script("document.body.style.zoom = '1.0'")
                    self.sleep(10)
        except (NoSuchWindowException,
                InvalidSessionIdException,
                WebDriverException) as err:
            print("Error message : %r" % err)

    @staticmethod
    def startBrowser():
        http_url = [
            "http://192.168.0.38/sp",
            "http://192.168.0.38/sp/symbolSchema/schemaDetached/?id=321&purposeGroup=3&equipId=10",
        ]
        errorMessages = [
            "http://192.168.0.38/sp",
            "http://192.168.0.38/sp/Error/Error404",
        ]
        path = [
            r'D:\AllCode\Python\python_apps\MTS\33kmMTS\html\start.html',
        ]

        options = webdriver.ChromeOptions()

        options.headless = False
        options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                             "/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36")
        options.add_argument("--no-default-browser-check")
        options.add_argument("--disable-audio-output")
        options.add_argument("--disable-audio-input")
        options.add_argument("--disable-gpu")
        options.add_argument("--no-sandbox")
        options.add_argument("--incognito")
        # options.add_argument("--kiosk")

        SeleniumExplorer = Browser(http_url, key=decrypted, options=options, path=path)
        SeleniumExplorer.startWindows()
        SeleniumExplorer.freshWindows(errorMessages=errorMessages)


if __name__ == '__main__':
    Browser.startBrowser()
