from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://www.goibibo.com/")
driver.maximize_window()


driver.execute_cdp_cmd(
    "Browser.setPermission",
    {
        "permission": {"name": "notifications"},
        "setting": "denied",
        "origin": "https://www.goibibo.com"
    }
)

driver.implicitly_wait(5)
driver.find_element(By.XPATH," //span[contains(@class, 'icClose')]").click()
driver.implicitly_wait(5)
driver.find_element(By.XPATH,"//span[text()='Departure']").click()

