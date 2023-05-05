import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

driver.get('https://www.google.com/')
time.sleep(3)
print("Current session is {}".format(driver.session_id))
driver.close()

try:
    driver.get("https://www.google.com/")
except Exception as e:
    print(e.message)