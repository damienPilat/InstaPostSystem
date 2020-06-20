import os
from time import sleep
from selenium import webdriver
from dotenv import load_dotenv
load_dotenv()

# Initialise Firefox as driver
browser = webdriver.Firefox()
browser.implicitly_wait(5)      # Wait for content to load if next task not found on page

# Enters url and hits enter
browser.get('https://www.instagram.com/')

# Look for and click login link (already on login page)
# login_link = browser.find_element_by_xpath("//a[text()='Log in']")
# login_link.click()

sleep(2)    # Load Page

# Find usr & pwd field, submit keys
browser.find_element_by_css_selector("input[name='username']").send_keys(os.getenv("USERNAME"))
browser.find_element_by_css_selector("input[name='password']").send_keys(os.getenv("PASSWORD"))
# Submit login
login_button = browser.find_element_by_xpath("//button[@type='submit']").click()
# Disregard Notification
browser.find_element_by_xpath("//button[text()='Not Now']").click()
# Go to Profile Page
browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]').click()

sleep(10)    # Keep page loaded

# Close Browser
browser.close()
