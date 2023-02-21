from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument('--start-maximized')
svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc,options=options)
driver.get("https://selectorshub.com/xpath-practice-page/")
wait = WebDriverWait(driver,30)

driver.quit()
