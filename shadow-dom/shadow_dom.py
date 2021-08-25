import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


## get the shadow root of any element
def select_shadow_element_by_css_selector(selector):
    run_this_script = 'return document.querySelector("%s").shadowRoot' %selector
    element = driver.execute_script(run_this_script)
    return element

def expand_shadow_root(element):
    shadow_root = driver.execute_script('return arguments[0].shadowRoot', element)
    return shadow_root


svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()
driver.get("https://www.virustotal.com/gui/file/03d1316407796b32c03f17f819cca5bede2b0504ecdb7ba3b845c1ed618ae934/details")

wait = WebDriverWait(driver, 20)
time.sleep(10)


root2 = driver.find_element(By.ID,'file-view')
shadow_root_2 = expand_shadow_root(root2)

root3 = shadow_root_2.find_element(By.ID,'report')
shadow_root_3 = expand_shadow_root(root3)

root4 = shadow_root_3.find_element(By.CSS_SELECTOR,'vt-ui-button[data-route="detection"]')
root4.click()

time.sleep(2)

driver.quit()
