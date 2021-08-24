from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time
options = Options()
options.add_argument('--allow-running-insecure-content')
options.add_argument('--ignore-certificate-errors')
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),options=options)
driver.maximize_window()
driver.get('https://cacert.org/')
print(driver.title)
time.sleep(3)

driver.quit()