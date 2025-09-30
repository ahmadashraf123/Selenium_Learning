from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

class hiddenElement:

    def elem_displayed(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.w3schools.com/howto/howto_js_toggle_hide_show.asp")
        display = driver.find_element(By.XPATH,"//div[@id='myDIV']").is_displayed()
        print(display)

        driver.find_element(By.XPATH," //button[normalize-space()='Toggle Hide and Show']").click()
        time.sleep(2)

        display1 = driver.find_element(By.XPATH, "//div[@id='myDIV']").is_displayed()
        print(display1)



        driver.quit()

view_obj = hiddenElement()
view_obj.elem_displayed()

