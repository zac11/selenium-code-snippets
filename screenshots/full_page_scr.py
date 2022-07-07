from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()
driver.get('https://testerops.com/')
time.sleep(5) #used because Chrome 103 has issues
driver.save_screenshot("full_page_scr.png")


driver.quit()