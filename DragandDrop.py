import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class DragAndDrop:
    def DROP(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://jqueryui.com/droppable/")
        driver.maximize_window()

        driver.switch_to.frame(driver.find_element(By.XPATH,"//iframe[@class='demo-frame']"))
        elem1 = driver.find_element(By.ID,"draggable")
        elem2 = driver.find_element(By.ID,"droppable")
        # ActionChains(driver).drag_and_drop(elem1, elem2).perform()
        time.sleep(3)

move = DragAndDrop()
move.DROP()