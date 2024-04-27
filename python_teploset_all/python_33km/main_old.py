# Tested on Python 3.11, Windows 10 64bit

from selenium.common.exceptions import (NoSuchWindowException,
                                        InvalidSessionIdException,
                                        WebDriverException, )
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from settings import decrypted
from selenium import webdriver
from time import sleep


class Browser:

    def __init__(self, http_url, key, options):
        self.key = key
        self.url = http_url
        self.sleep = sleep
        self.options = options

        # First window, set on 33km x=-1900, y=0
        self.driver = webdriver.Chrome(service=Service("drivers/chrome/chromedriver.exe"), options=self.options)
        self.driver.set_window_size(width=250, height=250)
        self.driver.set_window_position(x=0, y=0)
        self.driver.fullscreen_window()
        self.driver.get(self.url[0])

        # Last window, Set on 33km x=0, y=0
        self.driver_ = webdriver.Chrome(service=Service("drivers/chrome/chromedriver.exe"), options=self.options)
        self.driver_.set_window_size(width=250, height=250)
        self.driver_.set_window_position(x=2000, y=0)
        self.driver_.fullscreen_window()
        self.driver_.get(self.url[0])

    def startWindows(self):
        try:
            # Firsts
            self.driver.find_element(By.XPATH, "//input[@type='text']").send_keys(self.key)
            self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(self.key)
            self.driver.find_element(By.XPATH, "//input[@type='submit']").click()
            self.sleep(2)
            self.driver.execute_script(f"window.open('{self.url[1]}')")

            CDWindow_0 = self.driver.window_handles[0]
            CDWindow_1 = self.driver.window_handles[1]

            self.driver.switch_to.window(CDWindow_0)
            self.driver.close()
            self.driver.switch_to.window(CDWindow_1)
            self.driver.fullscreen_window()

            # Last
            self.driver_.find_element(By.XPATH, "//input[@type='text']").send_keys(self.key)
            self.driver_.find_element(By.XPATH, "//input[@type='password']").send_keys(self.key)
            self.driver_.find_element(By.XPATH, "//input[@type='submit']").click()
            self.sleep(2)
            self.driver_.execute_script(f"window.open('{self.url[2]}')")

            CDWindow_2 = self.driver_.window_handles[0]
            CDWindow_3 = self.driver_.window_handles[1]

            self.driver_.switch_to.window(CDWindow_2)
            self.driver_.close()
            self.driver_.switch_to.window(CDWindow_3)
            self.driver_.fullscreen_window()
        except Exception as ex:
            print(ex)

    def freshWindows(self, errorMessages):
        try:
            index = 0
            while (http_strings := [self.driver.current_url, self.driver_.current_url]) != 0:
                if (errorMessages[0] == self.driver.current_url
                        or errorMessages[0] == self.driver_.current_url
                        or errorMessages[1] == self.driver.current_url
                        or errorMessages[1] == self.driver_.current_url):
                    print("Error links : %r" % http_strings)
                    self.driver.close()
                    self.driver.quit()

                    self.driver_.close()
                    self.driver_.quit()
                    Browser.startBrowser()
                    break
                else:
                    index += 1
                    print(f"\n[count: {index}] Opened links : %r" % http_strings)

                    # # Screenshots create.
                    # self.driver.save_screenshot(f"screenshots\Window.png")
                    # self.driver_.save_screenshot(f"screenshots\Window_.png")
                    # print("Screenshots saved to : locale dir")

                    # Reload pages.
                    self.driver.refresh()
                    self.driver.execute_script("document.body.style.zoom = '0.95'")
                    self.driver.fullscreen_window()

                    self.driver_.refresh()
                    self.driver_.execute_script("document.body.style.zoom = '0.95'")
                    self.driver_.fullscreen_window()
                    self.sleep(10)
        except (NoSuchWindowException,
                InvalidSessionIdException,
                WebDriverException) as err:
            print("Error message : %r" % err)

    @staticmethod
    def startBrowser():
        http_url = ["http://192.168.0.38/sp",
                    "http://192.168.0.110/sp/symbolSchema/schema/?id=311&type=3&equipId=1",
                    "http://192.168.0.110/sp/symbolSchema/schema/?id=310&type=3&equipId=1", ]
        errorMessages = ["http://192.168.0.110/sp",
                         "http://192.168.0.110/sp/api/v1/Error/Error404", ]

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
        options.add_argument("--kiosk")

        SeleniumExplorer = Browser(http_url, key=decrypted, options=options)
        SeleniumExplorer.startWindows()
        SeleniumExplorer.freshWindows(errorMessages=errorMessages)


if __name__ == '__main__':
    Browser.startBrowser()
