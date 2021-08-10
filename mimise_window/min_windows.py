from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://blog.logrocket.com/a-guide-to-css-pseudo-elements/')
wait = WebDriverWait(driver, 20)
driver.minimize_window()
driver.maximize_window()
driver.implicitly_wait(10)
driver.set_window_position(0,0)
driver.quit()