from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.ag-grid.com/")
time.sleep(5)
all_names =[]
all_countries=[]
all_proficiency=[]
grid_row_xpath=driver.find_element_by_xpath("//div[@id='bestHtml5Grid']//div[@name='center']//div[@role='rowgroup']");
driver.find_element_by_xpath("//div[@id='bestHtml5Grid']//div[@name='center']//div[@role='rowgroup']").click()
all_div_elements = grid_row_xpath.find_elements_by_css_selector("div[role='row']")
print("all elements",len(all_div_elements))
for i in range(len(all_div_elements)):
    all_text = all_div_elements[i].find_element_by_css_selector("div[col-id='name']").text
    print("Name in graph ------->",all_text)
    all_names = all_names.append(all_text)
    country = all_div_elements[i].find_element_by_css_selector("div[col-id='country']").text
    print("Country in graph---->",country)
    all_countries = all_countries.append(country)
    proficient = all_div_elements[i].find_element_by_css_selector("div[col-id='proficiency'] div div:nth-child(2)").text
    print("Proficiency percentage",proficient)
    all_proficiency = all_proficiency.append(proficient)

driver.quit()