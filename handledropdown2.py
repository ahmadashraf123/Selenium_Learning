from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time

# Setup ChromeDriver using webdriver_manager (no need to download manually)
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Maximize the browser window
driver.maximize_window()

# Open Facebook signup page
driver.get("https://www.facebook.com")

# Click on 'Create new account' button to open the signup form
driver.find_element(By.XPATH, '//a[text() ="Create new account"]').click()

# Wait for the signup form to load
time.sleep(3)

# Locate the Month dropdown by ID
month = driver.find_element(By.ID, 'month')

# Create a Select object for the month dropdown to access its options
monthDD = Select(month)

# Get the first selected option (default selected month)
first_item = monthDD.first_selected_option
print("first selected option in dropdown is:", first_item.text)

# Assert to check if the first selected option is "Jul"
# This will raise an error if it's not "Jul"
assert "Jul" == first_item.text

# Get all the available options in the month dropdown
mylist = monthDD.options

# Print the total number of options (months)
print(len(mylist))

# Loop through each month option and print the month name
# If "Nov" is found, click on it and break the loop
for ele in mylist:
    print("value of:", ele.text)
    if ele.text == "Nov":
        ele.click()
        break
