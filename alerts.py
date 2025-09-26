import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class DemoPopup:

    def Demo_Alerts(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_prompt")
        driver.maximize_window()
        driver.switch_to.frame("iframeResult")

        # Case 1: Accept without input
        driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
        time.sleep(2)
        print(driver.switch_to.alert.text)
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)

        # # Case 2: Dismiss
        # driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert.dismiss()
        # time.sleep(2)
        #
        # # Case 3: Send text to prompt and accept
        # driver.find_element(By.XPATH, "//button[@onclick='myFunction()']").click()
        # time.sleep(2)
        # alert = driver.switch_to.alert
        # alert.send_keys("ahmad")
        # time.sleep(1)
        # alert.accept()
        # time.sleep(2)

        driver.quit()

w_alerts = DemoPopup()
w_alerts.Demo_Alerts()
