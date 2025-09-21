import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class CaptureScreenshot:

    def capture(self):
        # Setup Chrome browser
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # Open Facebook login page
        driver.get('https://www.facebook.com/')
        driver.maximize_window()
        time.sleep(2)

        # Capture screenshot of the login button
        login_button = driver.find_element(By.NAME, "login")
        login_button.screenshot("./login_button.png")
        print("Screenshot of login button saved as login_button.png")

        # Click on login button (without entering credentials)
        login_button.click()
        time.sleep(2)

        # Capture full page screenshot after click
        driver.save_screenshot("./full_page.png")
        print("Full page screenshot saved as full_page.png")

        # Close the browser
        driver.quit()

# Run the class method
screenshot_taker = CaptureScreenshot()
screenshot_taker.capture()
