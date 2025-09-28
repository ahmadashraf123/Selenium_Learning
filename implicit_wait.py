import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DemoImplicitWait():
    def demo_imp_wait(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.implicitly_wait(10)
        driver.get("https://login.salesforce.com/?locale=eu")
        driver.maximize_window()
        driver.find_element(By.ID,"username").send_keys("Ahmad")


W8 = DemoImplicitWait()
W8.demo_imp_wait()