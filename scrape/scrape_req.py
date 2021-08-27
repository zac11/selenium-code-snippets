## For StackOverflow question - https://stackoverflow.com/questions/68951623/scrape-complete-information-of-all-companies-using-api-requests-in-python/68952162?noredirect=1#comment121861850_68952162
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import  requests

svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()
driver.get("https://www.spacresearch.com/symbol?s=live-deal&sector=&geography=")

wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'tbody tr')))

listofcompanies= []
get_all_company_rows = driver.find_elements(By.TAG_NAME,'tbody tr')
print(len(get_all_company_rows))
time.sleep(5)
for i in range(len(get_all_company_rows)):
    nameofcompanies = get_all_company_rows[i].find_element(By.CSS_SELECTOR,'td:nth-child(3)').text
    #print(nameofcompanies)
    listofcompanies.append(nameofcompanies)

def get_company(root_symbol):
    end_point = "https://www.spacresearch.com/api/v1/company/{}".format(root_symbol)
    print("Connecting to: ", end_point)
    token = "Bearer {}".format('YOUR_API_TOKEN')
    return requests.get(end_point, headers={"Authorization": token})

print(listofcompanies)
for i in range(len(listofcompanies)):
    response_json = get_company(listofcompanies[i]).json()
    print(response_json)


driver.quit()