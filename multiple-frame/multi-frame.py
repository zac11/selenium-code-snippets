from selenium import webdriver
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('https://tn.tunisiebooking.com/')
wait = WebDriverWait(driver, 20)

# params to select
params = {
    'destination': 'Sfax',
    'date_from': '08/08/2021',
    'date_to': '09/08/2021',
    'bedroom': '1'
}

# select destination
destination_select = Select(driver.find_element_by_id('ville_des'))
destination_select.select_by_value(params['destination'])

# select bedroom
bedroom_select = Select(driver.find_element_by_id('select_ch'))
bedroom_select.select_by_value(params['bedroom'])

# select dates
script = f"document.getElementById('depart').value ='{params['date_from']}';"
script += f"document.getElementById('checkin').value ='{params['date_to']}';"
driver.execute_script(script)

# click bouton search
btn_rechercher = driver.find_element_by_css_selector("div[onclick='return submit_hotel_recherche()']")
btn_rechercher.click()
time.sleep(10)
child = "div#facerd > div:nth-child(3) > div:nth-child(2) > div > div > div"
textid="label"
all_results_deiv = driver.find_elements_by_css_selector("div#ruslt > div")
labeltext = driver.find_elements_by_css_selector("div[class='typechambre'] label")
print(len(all_results_deiv))
'''

for i in range(len(all_results_deiv)):
    facecard = all_results_deiv[i].find_element_by_css_selector(child).text
    labelte = all_results_deiv[i].find_elements_by_css_selector('label')
    print(facecard)
    for j in range(len(labelte)):
        print(labelte[j].text)
'''

## another section
for x in range(len(all_results_deiv)):
    checkboxele = all_results_deiv[x].find_elements_by_css_selector("input[type='radio']")
    print(len(checkboxele))
    for y in range(len(checkboxele)):
        driver.execute_script("arguments[0].setAttribute('style', arguments[1]);",checkboxele[y])
        #checkboxele[y].click()
        facecard1 = all_results_deiv[x].find_element_by_css_selector(child).text
        print(facecard1)







driver.quit()