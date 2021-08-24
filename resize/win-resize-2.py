from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import ChromiumOptions
from webdriver_manager.chrome import ChromeDriverManager
import time
options = ChromiumOptions()
options.add_argument('--window-size=1400x900')
svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()
print(driver.get_window_size())
driver.get('https://yizeng.me/2014/02/23/how-to-get-window-size-resize-or-maximize-window-using-selenium-webdriver/')
time.sleep(5)

driver.quit()