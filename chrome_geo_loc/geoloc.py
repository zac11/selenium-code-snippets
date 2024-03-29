
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

params ={
    "latitude": 28.53110,
    "longitude": 77.38926,
    "accuracy" : 100
}

svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()
driver.get('https://grofers.com/')
time.sleep(5)
driver.find_element(By.CSS_SELECTOR,"button[class='btn location-box mask-button']").click()
time.sleep(5)
driver.execute_cdp_cmd('Emulation.setGeolocationOverride',params)
time.sleep(5)

driver.quit()