from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)


driver.get("https://www.youtube.com/")
driver.implicitly_wait(5)

search_box = driver.find_element(By.NAME, "search_query")
search_box.send_keys("selenium")


