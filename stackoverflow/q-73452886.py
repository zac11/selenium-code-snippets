# Stackoverflow question link https://stackoverflow.com/questions/73173658/element-not-interactable-object-svggelement-has-no-size-and-location-selenium
import time
from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


svc = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.fullscreen_window()

def highlight(element):
    """Highlights a Selenium webdriver element"""
    driver = element._parent
    def apply_style(s):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1])", element, s)
    orignal_style = element.get_attribute('style')
    apply_style("border: 4px solid red")
    if (element.get_attribute("style")!=None):
        time.sleep(5)
    apply_style(orignal_style)


driver.get("https://www.untiedau.com/products/nike-dunk-low-triple-pink-womens-gs")
time.sleep(5)
#search = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "product-single__swatch-product-template-1-us7-5w-us6y")))
size_elem = driver.find_element(By.CSS_SELECTOR,"label[for='product-single__swatch-product-template-1-us7-5w-us6y']")

highlight(size_elem)
driver.find_element(By.ID, "element")
size_elem.click()
time.sleep(5)


driver.quit()