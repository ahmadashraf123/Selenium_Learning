import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class RightClickDoubleClick:
    def RightClick(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://demo.guru99.com/test/simple_context_menu.html")
        driver.maximize_window()
        # elem1 = driver.find_element(By.XPATH,"//span[@class='context-menu-one btn btn-neutral']")
        # copyelement = driver.find_element(By.XPATH,"//span[normalize-space()='Copy']")
        # actions = ActionChains(driver)
        # actions.context_click(elem1).perform()
        # time.sleep(3)
        # copyelement.click()
        # time.sleep(3)


        doubleelement = driver.find_element(By.XPATH,"//button[normalize-space()='Double-Click Me To See Alert']")
        Actions = ActionChains(driver)
        Actions.double_click(doubleelement).perform()
        time.sleep(3)


click=RightClickDoubleClick()
click.RightClick()
