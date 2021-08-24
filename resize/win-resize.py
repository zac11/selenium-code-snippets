from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()
print(driver.get_window_size())
driver.get('https://yizeng.me/2014/02/23/how-to-get-window-size-resize-or-maximize-window-using-selenium-webdriver/')
driver.set_window_size(480,320)
print(driver.get_window_size())
time.sleep(5)
driver.set_window_size(1400,900)
time.sleep(5)

driver.quit()