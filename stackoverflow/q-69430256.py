# Stackoverflow question link https://stackoverflow.com/questions/69430256/selenium-can-not-get-url-from-product-page

from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
svc=  Service(ChromeDriverManager().install())
options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(service=svc,options=options)
driver.maximize_window()


driver.get("https://www.falabella.com/falabella-cl/collection/ofertas-mujer-ropa-v2")
wait = WebDriverWait(driver,30)
wait.until(EC.visibility_of_element_located((By.ID,'testId-Dropdown-desktop-button')))

sectionclass = driver.find_element(By.ID,"testId-searchResults-products")
alldivs = sectionclass.find_elements(By.CSS_SELECTOR,"div.jsx-4001457643.search-results-4-grid.grid-pod")

for i in range(len(alldivs)):
    all_text = alldivs[i].find_element(By.CSS_SELECTOR,'div > a').get_attribute("href")
    print(all_text)


driver.quit()