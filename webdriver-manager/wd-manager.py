from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.get('https://stackoverflow.com/')
time.sleep(5)
print(driver.title)
driver.quit()