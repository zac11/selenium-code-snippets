import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()
driver.get("https://www.spacresearch.com/symbol?s=live-deal&sector=&geography=")

wait = WebDriverWait(driver, 20)
#time.sleep(10)

wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.container-lg.p-responsive.text-center.py-6')))
countofrepos = driver.find_elements(By.TAG_NAME,'article')
print('There are %s trending repos today' %len(countofrepos))

## get all repos name
for i in range(len(countofrepos)):
    repo_name = countofrepos[i].find_element(By.CSS_SELECTOR,'.h3.lh-condensed > a').text
    print(repo_name)
    stars = countofrepos[i].find_elements(By.CSS_SELECTOR,'div')
    for j in range(len(stars))[1:]:
        starscount = stars[j].find_element(By.CSS_SELECTOR,'a').text
        print('There are %s stars'%(starscount),'for this repo')
        todaycount = stars[j].find_element(By.CSS_SELECTOR,'span[class="d-inline-block float-sm-right"]').text
        print('%s has currently %s '%(repo_name,todaycount))


driver.quit()