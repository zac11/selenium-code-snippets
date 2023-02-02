from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument('--kiosk')
svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc,options=options)
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.implicitly_wait(20)

driver.quit()
