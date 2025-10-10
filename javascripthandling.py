import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoJs:

    def Demo_javascript(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        #driver.get("https://training.rcvacademy.com")
        driver.execute_script("window.open('https://training.rcvacademy.com','_self')")
        time.sleep(5)


js=DemoJs()
js.Demo_javascript()