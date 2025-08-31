import time
from calendar import Month

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

from selenium.webdriver.support.select import Select

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

driver.maximize_window()

driver.get("https://www.facebook.com")

driver.find_element(By.XPATH, '//a[text() ="Create new account"]').click()
time.sleep(3)
driver.find_element(By.NAME,"firstname").send_keys("Ahmad")
driver.find_element(By.NAME,"lastname").send_keys("khan")

Day=Select(driver.find_element(By.XPATH,'//select[@title="Day"]'))
Day.select_by_visible_text('4')
month=Select(driver.find_element(By.XPATH,'//select[@title="Month"]'))
month.select_by_visible_text('Nov')
birthyear=Select(driver.find_element(By.XPATH,'//select[@title="Year"]'))
birthyear.select_by_visible_text('2000')
driver.find_element(By.XPATH,'//label[text()="Male"]').click()
driver.find_element(By.NAME,'reg_email__').send_keys("<ahmad@gmail.com>")
driver.find_element(By.NAME,'reg_passwd__').send_keys("<Skill#123>")
driver.find_element(By.XPATH,'//button[text()="Sign Up"]').click()