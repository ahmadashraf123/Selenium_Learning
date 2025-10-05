import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


class HandleSlider:
    def Slider(self):
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)
        driver.get("https://jqueryui.com/slider/")
        driver.maximize_window()

        # Switch to iframe containing the slider
        iframe = driver.find_element(By.XPATH, "//iframe[@class='demo-frame']")
        driver.switch_to.frame(iframe)

        # Now find the slider handle inside the iframe
        slider_handle = driver.find_element(By.XPATH, "//div[@id='slider']/span")

        # Move the slider
        actions = ActionChains(driver)
        actions.click_and_hold(slider_handle).move_by_offset(100, 0).release().perform()

        time.sleep(5)
        driver.quit()

# Run it
SLD = HandleSlider()
SLD.Slider()
