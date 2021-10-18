from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()
driver.get('https://github.com/SeleniumHQ/selenium')
time.sleep(5)
# create a new tab in same chrome window and switch focus
driver.switch_to.new_window('tab')
driver.get("https://www.swtestacademy.com")
time.sleep(3)

# create a new chrome instance (new window) and then switch focus to that window
driver.switch_to.new_window('window')
driver.get('https://github.com/trending')
time.sleep(3)

driver.quit()