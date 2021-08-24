from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get('https://mdn.github.io/learning-area/html/forms/editable-input-example/editable_input.html')
driver.find_element_by_id('input1').send_keys('user name python 2')
driver.find_element_by_id('input2').send_keys("ocean", Keys.SPACE, "sie", Keys.LEFT, "d")
time.sleep(5)
driver.quit()

