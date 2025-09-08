import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class single_dropdown:
    def dropdown(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.facebook.com")
        driver.find_element(By.XPATH, '//a[text() ="Create new account"]').click()
        time.sleep(3)
        day = driver.find_element(By.ID, "day")
        day_dropdown =Select(day)
        day_dropdown.select_by_index(3)
        time.sleep(3)
        day_dropdown.select_by_value("7")
        time.sleep(3)
        day_dropdown.select_by_visible_text("14")
        time.sleep(3)
demo_dropdown = single_dropdown()
demo_dropdown.dropdown()

