from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
options = Options()
options.add_argument('--headless')
svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc,options=options)
driver.set_window_size(1400,900)
driver.get("https://www.ouedkniss.com/")
wait = WebDriverWait(driver,30)
wait.until(EC.visibility_of_element_located((By.ID,'menu_recherche_query')))

search_bar = driver.find_element(By.ID,'menu_recherche_query')
search_bar.click()
search_bar.send_keys('golf 6')
search_button = driver.find_element(By.ID,'menu_recherche_submit')
search_button.click()
driver.save_screenshot('headfull.png')

driver.quit()
