from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
import time
desired_caps = DesiredCapabilities.CHROME.copy()
desired_caps['acceptInsecureCerts'] = True

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(),desired_capabilities=desired_caps)
driver.maximize_window()
driver.get('https://cacert.org/')
print(driver.title)
time.sleep(3)

driver.quit()