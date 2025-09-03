from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

class LocatorPractice:

    def __init__(self):
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)

    def test_all_locators(self):
        self.driver.get("https://www.selenium.dev/selenium/web/web-form.html")
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

        # ID
        self.driver.find_element(By.ID, "my-text-id").send_keys("Testing ID")

        # NAME
        self.driver.find_element(By.NAME, "my-password").send_keys("Test1234")

        # CLASS NAME
        self.driver.find_element(By.CLASS_NAME, "form-check-input").click()

        # TAG NAME
        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        print(f"Found {len(inputs)} input fields")

        # LINK TEXT
        self.driver.find_element(By.LINK_TEXT, "Return to index").click()
        self.driver.back()

        # PARTIAL LINK TEXT
        self.driver.find_element(By.PARTIAL_LINK_TEXT, "Return").click()
        self.driver.back()

        # CSS SELECTOR
        self.driver.find_element(By.CSS_SELECTOR, "input[name='my-text']").send_keys("CSS Test")

        # XPATH
        self.driver.find_element(By.XPATH, "//textarea[@name='my-textarea']").send_keys("XPath Test")

        time.sleep(3)

    def close_browser(self):
        self.driver.quit()

# Run the test
test = LocatorPractice()
test.test_all_locators()
test.close_browser()
