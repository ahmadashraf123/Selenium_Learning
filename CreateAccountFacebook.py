import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Set Chrome options (important for Jenkins/CI)
options = Options()
# options.add_argument("--headless=new")       # Run headless (no browser window)
options.add_argument("--no-sandbox")         # Prevents sandbox errors in Jenkins
options.add_argument("--disable-dev-shm-usage")  # Avoids memory issues
options.add_argument("--disable-gpu")        # Optional: stabilize headless mode

# Use webdriver-manager to get correct driver
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.maximize_window()
driver.get("https://www.facebook.com")

driver.find_element(By.XPATH, '//a[text() ="Create new account"]').click()
time.sleep(3)

driver.find_element(By.NAME, "firstname").send_keys("Ahmad")
driver.find_element(By.NAME, "lastname").send_keys("Khan")

day = Select(driver.find_element(By.XPATH, '//select[@title="Day"]'))
day.select_by_visible_text('4')

month = Select(driver.find_element(By.XPATH, '//select[@title="Month"]'))
month.select_by_visible_text('Nov')

year = Select(driver.find_element(By.XPATH, '//select[@title="Year"]'))
year.select_by_visible_text('2000')

driver.find_element(By.XPATH, '//label[text()="Male"]').click()
driver.find_element(By.NAME, 'reg_email__').send_keys("ahmad@gmail.com")
driver.find_element(By.NAME, 'reg_passwd__').send_keys("Skill#123")

driver.find_element(By.XPATH, '//button[text()="Sign Up"]').click()

print("✅ Facebook account creation test executed successfully")

driver.quit()
