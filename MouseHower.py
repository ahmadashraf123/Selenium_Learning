import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class NawaahLogin:
    def __init__(self, auth_username, auth_password):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.auth_username = auth_username
        self.auth_password = auth_password

    def nawah_auth_login(self):
        url = f"https://{self.auth_username}:{self.auth_password}@dev.nawaah.com/sign-in"
        self.driver.get(url)

    def web_login(self, email, password):
        self.driver.maximize_window()
        time.sleep(5)

        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()
        time.sleep(5)  # Increased time to ensure sidebar loads

    def Performance_Mouse_Hower(self):
        time.sleep(5)  # Ensure sidebar is rendered
        analytics = self.driver.find_element(By.XPATH, "//a[.//h6[text()='Analytics']]")
        action = ActionChains(self.driver)
        action.move_to_element(analytics).perform()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "(//h6[normalize-space()='Performance Insights'])[1]").click()
        time.sleep(2)
        self.driver.back()
        time.sleep(2)

# Usage
login = NawaahLogin(auth_username="nawaah-dev", auth_password="M4ymgi2Z1GMC")
login.nawah_auth_login()
login.web_login("demo@yopmail.com", "Nawah12@")
login.Performance_Mouse_Hower()
