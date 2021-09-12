import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()
driver.get("https://www.galaxus.ch/search?q=5010533606001")

wait = WebDriverWait(driver, 20)
#time.sleep(10)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'article > a')))
driver.find_element(By.CSS_SELECTOR,'article > a').click()
time.sleep(10)

driver.quit()