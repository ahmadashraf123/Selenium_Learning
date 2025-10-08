from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Element_state:

    def enabled_state(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://training.openspan.com/login")
        state = driver.find_element(By.XPATH,"//input[@id='login_button']").is_enabled()
        print(state)

        driver.find_element(By.XPATH," //input[@id='user_name']").send_keys("username")
        time.sleep(2)
        driver.find_element(By.XPATH," //input[@id='user_pass']").send_keys("password")
        time.sleep(2)

        state1 = driver.find_element(By.XPATH, "//input[@id='login_button']").is_enabled()
        print(state1)



        driver.quit()

state_obj = Element_state()
state_obj.enabled_state()

