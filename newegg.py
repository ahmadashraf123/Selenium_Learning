import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class MultipleWindowDemo:

    def handle_multiple_windows(self):
        # Setup Chrome WebDriver using ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # Open the Guru99 demo site
        driver.get("https://www.newegg.com/?srsltid=AfmBOorNdspWG8ZNvAaabxS-JjfqMsRK2w_6trT49qrCJo0CF200cnwu")
        driver.maximize_window()
        time.sleep(5)
demo = MultipleWindowDemo()
demo.handle_multiple_windows()