from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
svc=Service(ChromeDriverManager().install())
options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
web = webdriver.Chrome(service=svc,options=options)
web.maximize_window()
web.get('https://msbte.org.in/DISRESLIVE2021CRSLDSEP/frmALYSUM21PBDisplay.aspx')
wait = WebDriverWait(web,20)
# variable to store the result
resultCount = 0

rlstart = 156857
rlend = 157299

try:
    for x in range(rlend):
        orginal_window = web.current_window_handle
        seat_input_box = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, "input[id='txtEnrollSeatNo']")))
        time.sleep(1)
        seat_input_box.clear()
        seat_input_box.send_keys(rlstart)
        rlstart = rlstart + 1
        submit = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[id='btnSubmit']")))
        submit.click()
        try:
            if wait.until(EC.alert_is_present) == True:
                print("Means alert is present. ")
                a = web._switch_to.alert
                a.accept()
                web.switch_to.default_content()
            else:
                print("Alert was not present, but new windows was")
                handles = web.window_handles
                web.switch_to.window(handles[1])
                time.sleep(1)
                web.maximize_window()
                time.sleep(2)
                web.execute_script("window.scrollTo(0, 300)")
                time.sleep(2)
                getresult = wait.until(EC.presence_of_element_located((By.XPATH, "//td[contains(text(),'Aggregate Marks : ')]/following-sibling::td[2]/strong"))).text
                getresult_dec = float(getresult)
                if getresult_dec > 96.00 :
                    resultCount = resultCount + 1
                    print("Kill the browser in else block.")
                    web.close()
                else:
                    web.close()
                    print("Kill the browser in else block.")
        except:
            pass
        time.sleep(3)
        web.switch_to.window(orginal_window)

except:
    pass