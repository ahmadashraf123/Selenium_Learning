import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

class MultipleWindowDemo:

    def handle_multiple_windows(self):
        # Setup Chrome WebDriver using ChromeDriverManager
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service)

        # Open the Guru99 demo site
        driver.get("https://demo.guru99.com/popup.php")
        driver.maximize_window()

        # Store the parent window handle for later use
        parent_window_handle = driver.current_window_handle
        print("Parent Window Handle:", parent_window_handle)

        # Click on the "Click Here" link to open a new window
        driver.find_element(By.XPATH, "//a[normalize-space()='Click Here']").click()
        time.sleep(3)  # Give time for the new window to open

        # Get all window handles (parent + child windows)
        all_window_handles = driver.window_handles
        print("All Window Handles:", all_window_handles)

        # Loop through all handles and switch to the child window
        for window_handle in all_window_handles:
            if window_handle != parent_window_handle:
                driver.switch_to.window(window_handle)
                print("Switched to Child Window:", window_handle)

                # Interact with the child window (enter email)
                driver.find_element(By.XPATH, "//input[@name='emailid']").send_keys("ahmad@yopmail.com")
                time.sleep(5)

                # Close the child window
                driver.close()
                print("Child window closed")

        # Switch back to the parent window
        driver.switch_to.window(parent_window_handle)
        print("Switched back to Parent Window:", parent_window_handle)

        # Close the browser session
        driver.quit()

# Create an instance and run the method
demo = MultipleWindowDemo()
demo.handle_multiple_windows()
