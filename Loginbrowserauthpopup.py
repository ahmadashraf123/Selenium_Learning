# Import necessary libraries
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

# Class to handle Nawaah login
class NawaahLogin:

    def __init__(self, basic_auth_username, basic_auth_password):
        # Setup Chrome browser using WebDriverManager
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Save basic authentication details
        self.basic_auth_username = basic_auth_username
        self.basic_auth_password = basic_auth_password

    def login_with_basic_auth(self):
        # Use basic auth in URL to avoid popup
        url = f"https://{self.basic_auth_username}:{self.basic_auth_password}@dev.nawaah.com/sign-in"
        self.driver.get(url)

    def login_to_web_form(self, email, password):
        # Maximize window and wait for page to load
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        # Fill in the login form
        self.driver.find_element(By.NAME, "email").send_keys(email)
        self.driver.find_element(By.NAME, "password").send_keys(password)

        # Click the Sign In button
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def close_browser(self):
        # Close the browser window
        self.driver.quit()


# ==== Example Usage ====

# Step 1: Create the login object and pass Basic Auth credentials
login = NawaahLogin(basic_auth_username="nawaah-dev", basic_auth_password="M4ymgi2Z1GMC")

# Step 2: Login using Basic Auth (this removes the popup)
login.login_with_basic_auth()

# Step 3: Fill the email/password form shown on the website
login.login_to_web_form(email="Nawahstudent@yopmail.com", password="Nawah@12")

# Step 4: Close the browser
login.close_browser()
