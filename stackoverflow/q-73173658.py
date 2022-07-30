# Stackoverflow question link https://stackoverflow.com/questions/73173658/element-not-interactable-object-svggelement-has-no-size-and-location-selenium
import time
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

svc = Service(ChromeDriverManager().install())
options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=svc,options=options)
driver.maximize_window()


driver.get("https://youtube.com")
search = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "search")))

driver.find_element(By.NAME,'search_query').click()
time.sleep(5)

driver.find_element(By.NAME,'search_query').send_keys('Iktarfa')

button = driver.find_element(By.ID, "search-icon-legacy").click()

time.sleep(5)

driver.quit()