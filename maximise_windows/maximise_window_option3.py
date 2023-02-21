from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc,options=options)
driver.set_window_size(1400,900)
driver.get("https://selectorshub.com/xpath-practice-page/")
wait = WebDriverWait(driver,30)

driver.quit()
