from time import sleep
from selenium import webdriver

# Initialise Firefox as driver
browser = webdriver.Firefox()
browser.implicitly_wait(5)      # Wait for content to load if next task not found on page

# Enters url and hits enter
browser.get('https://www.instagram.com/')

# Look for and click login link (already on login page)
# login_link = browser.find_element_by_xpath("//a[text()='Log in']")
# login_link.click()

sleep(2)    # Load Page

# Find usr & pwd field
username_input = browser.find_element_by_css_selector("input[name='username']")
password_input = browser.find_element_by_css_selector("input[name='password']")
# Send usr & pwd
username_input.send_keys("USERNAME")
password_input.send_keys("PASSWORD")
# Submit
login_button = browser.find_element_by_xpath("//button[@type='submit']")
login_button.click()
# Disregard Notification
notification_button = browser.find_element_by_xpath("//button[text()='Not Now']")
notification_button.click()

sleep(50)    # Keep page loaded


# Close Browser
browser.close()
