from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
svc=Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=svc)
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.implicitly_wait(20)
driver.quit()
