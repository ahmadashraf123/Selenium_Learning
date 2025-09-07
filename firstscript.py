from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

# WebDriverManager automatically downloads correct ChromeDriver version
service = Service(ChromeDriverManager().install())

# Launch Chrome browser
driver = webdriver.Chrome(service=service)

# Open Google
driver.get("https://www.google.com")
time.sleep(3)

# Close browser
driver.quit()
