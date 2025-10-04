import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By



service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.get("https://nawaah.com/sign-in")
forget_password = driver.find_element(By.LINK_TEXT,"Forgot password")
forget_password.click()
