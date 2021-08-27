
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import ChromiumOptions
import time

options = ChromiumOptions()
options.add_argument('--disable-infobars')
options.add_argument("start-maximized")
options.add_argument("--disable-extensions")

options.add_experimental_option('prefs',{
    "profile.default_content_setting_values.notifications": 1
})

svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc,options=options)
driver.maximize_window()
driver.get('https://www.webpushr.com/demo')
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"div.row.mb-5 > div:nth-child(1)  img").click()
time.sleep(3)

driver.quit()