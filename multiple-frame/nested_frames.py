from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
import time
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://plnkr.co/edit/TilyvTTsKRyBnNutQQkf?preview')
wait = WebDriverWait(driver, 20)

seq = driver.find_elements_by_tag_name('iframe')
print("No of frames present in the web page are: ", len(seq))
for index in range(len(seq)):
    iframe = driver.find_elements_by_tag_name('iframe')[index]
    driver.switch_to.frame(iframe)
    print("swriched to iframe1")
    seq2 = driver.find_elements_by_tag_name('iframe')
    print(len(seq2))
    for index2 in range(len(seq2)):
        iframe2 = driver.find_elements_by_tag_name("iframe")[index2]
        driver.switch_to.frame(iframe2)
        print('Switched to iframe 2')
        time.sleep(2)
        driver.find_element_by_tag_name('button').click()
        time.sleep(2)
        seq3 = driver.find_elements_by_tag_name('iframe')
        print(len(seq3))
        for index3 in range(len(seq3)):
            iframe3 = driver.find_elements_by_tag_name('iframe')[index3]
            driver.switch_to.frame(iframe3)
            print('Switched to iframe 3')
            time.sleep(2)
            print(driver.find_element_by_tag_name('h1').text)
            driver.switch_to.parent_frame()
            driver.find_element_by_tag_name('button').click()
            time.sleep(2)
            ## find total no of frames now
            no_frames = driver.find_elements_by_tag_name('iframe')
            print('There are now',len(no_frames),' frames')
            driver.switch_to.default_content()








driver.quit()