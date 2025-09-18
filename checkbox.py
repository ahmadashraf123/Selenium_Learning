from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class checkbox:
    def elem_checkbox(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://staging.darkenergyai.com/users/sign_in")
        time.sleep(3)
        driver.find_element(By.XPATH,"   // input[ @ type = 'checkbox']").click()
        time.sleep(3)
        var1=driver.find_element(By.XPATH,"   // input[ @ type = 'checkbox']").is_selected()
        print(var1)
check=checkbox()
check.elem_checkbox()








