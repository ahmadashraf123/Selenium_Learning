from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class GetAttribute:

    def get_value(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.facebook.com/")

        # Use stable xpath or name selector
        attr_value = driver.find_element(By.XPATH, "//button[@name='login']").get_attribute("type")
        print(f"The type of the login button is: {attr_value}")

        time.sleep(2)
        driver.quit()

attr_obj = GetAttribute()
attr_obj.get_value()
