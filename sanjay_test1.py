import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


## get the shadow root of any element

def expand_shadow_root(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root


svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()
driver.get("https://selectorshub.com/xpath-practice-page/")


wait = WebDriverWait(driver, 20)
time.sleep(10)

f_iframe = driver.find_element(By.CSS_SELECTOR,'iframe#pact')

driver.switch_to.frame(f_iframe)

element = driver.execute_script('return document.querySelector(\"#jest\").shadowRoot.querySelector("#coffee")')
jsstring = driver.execute_script("arguments[0].setAttribute('value','Sanjay')",element)




driver.quit()


