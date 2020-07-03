import os
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import *
from selenium.webdriver.firefox.options import *
from dotenv import load_dotenv
load_dotenv()

# Set Options for Driver
options = Options()
options.add_argument('--user-agent=Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) CriOS/56.0.2924.75 Mobile/14E5239e Safari/602.1')
# Set Responsive Design Mode to iPhone
# options.set_capability("deviceName", "iPhone") # Not workning

# Initialise Firefox as driver
browser = webdriver.Firefox(options=options)
# Set Window position & siz
browser.set_window_position(0, 0)
browser.set_window_size(375, 812)

# Wait for content to load if next task not found on page
browser.implicitly_wait(5)

# Enters url and hits enter
browser.get('https://www.instagram.com/')

# Look for and click login link (already on login page)
# login_link = browser.find_element_by_xpath("//a[text()='Log in']")
# login_link.click()

sleep(2)    # Load Page

# Set Responsive Manually
action = ActionChains(browser)
action.send_keys(Keys.COMMAND, Keys.ALT, 'M')

# Find usr & pwd field, submit keys
browser.find_element_by_css_selector("input[name='username']").send_keys(os.getenv("USERNAME"))
browser.find_element_by_css_selector("input[name='password']").send_keys(os.getenv("PASSWORD"))
# Submit login
login_button = browser.find_element_by_xpath("//button[@type='submit']").click()
# Dont save credentials
browser.find_element_by_xpath("//button[text()='Not Now']").click()
# Disregard Notification
browser.find_element_by_xpath("//button[text()='Not Now']").click()

# Reload for mobile exp
browser.refresh()

# Go to Profile Page
# browser.find_element_by_xpath('/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]').click()

sleep(10)    # Keep page loaded

# Close Browser
browser.close()
