# Import necessary Selenium libraries
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

# Create a class to hold browser common actions
class browsercommond:

    # Define a method to perform multiple browser actions
    def browser_method(self):

        # Setup ChromeDriver using webdriver_manager (automatically installs correct version)
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # Open the given website
        driver.get("https://training.rcvacademy.com/")

        # Print the current URL in the console
        print(driver.current_url)

        # Print the page title in the console
        print(driver.title)

        # Maximize the browser window
        driver.maximize_window()

        # Make the browser fullscreen (this may hide toolbars, depends on OS/driver support)
        driver.fullscreen_window()

        # Refresh the current page
        driver.refresh()

        # Try to click a link using LINK_TEXT (This will fail because '<ALL COURSES>' is incorrect)
        # In real HTML, link text should be written without '< >'
        driver.find_element(By.LINK_TEXT, '<ALL COURSES>').click()

        # Go back to the previous page
        driver.back()

        # Go forward to the next page
        driver.forward()

        # Minimize the browser window
        driver.minimize_window()

        # Pause the script for 5 seconds so you can see the actions happening
        time.sleep(5)

        # Close the browser completely
        driver.quit()

# Create an object of the class and call the method to run the script
browser = browsercommond()
browser.browser_method()
