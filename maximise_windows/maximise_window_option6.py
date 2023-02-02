import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service



svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
max_width, max_height = driver.execute_script("return [window.screen.availWidth, window.screen.availHeight];")
print(max_width,max_height)
time.sleep(3)
driver.set_window_size(max_width,max_height)
driver.get("https://selectorshub.com/xpath-practice-page/")
driver.implicitly_wait(20)

driver.quit()
