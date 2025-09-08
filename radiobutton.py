from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class Radiobutton:
    def radio_box(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.w3schools.com/html/tryit.asp?filename=tryhtml_input_radio")
        time.sleep(3)

        driver.switch_to.frame("iframeResult")
        driver.find_element(By.XPATH,"//input[@id='html']").click()
        time.sleep(3)
        var1=driver.find_element(By.XPATH,"//input[@id='html']").is_selected()
        print(var1)
check=Radiobutton()
check.radio_box()



