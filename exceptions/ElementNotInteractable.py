import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

options = webdriver.ChromeOptions()

# options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

chrome_driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

with chrome_driver as driver:
    driver.implicitly_wait(15)
    driver.get('https://www.wagr.com/mens-ranking')
    time.sleep(3)

    # click cookie popup
    cookie_btn = driver.find_element(By.XPATH, "/html/body/div[2]/div[3]/div/div/div[2]/div[1]/button")
    cookie_btn.click()
    time.sleep(0.3)

    # scrolling bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(2)

    next_btn = driver.find_element(By.CSS_SELECTOR, "a[aria-label='Next page']")  # li.next
    # next_btn = driver.find_element(By.XPATH, "//li[@class='next']")
    time.sleep(4)

    print("found and click next", next_btn.tag_name)
    next_btn.click()

    time.sleep(2)
    driver.quit()