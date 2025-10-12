from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
import time

# Use WebDriver Manager for GeckoDriver
service = Service(GeckoDriverManager().install())

# Launch Firefox
driver = webdriver.Firefox(service=service)

# Open website
driver.get("https://www.firefox.com")

# Wait for 3 seconds
time.sleep(3)

# Close the browser
driver.quit()
