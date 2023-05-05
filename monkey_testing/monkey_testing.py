from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

options = Options()
options.page_load_strategy = 'normal'
svc=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()

driver.get("https://flipkart.com")

wait = WebDriverWait(driver, 20)
wait.until(EC.visibility_of_element_located((By.XPATH,"//a[normalize-space()='Login']")))

script = "javascript: (function() {" \
         "function callback() {" \
         "gremlins.createhorder({" \
         "species: [gremlins.species.clicker(), gremlins.species.toucher(), gremlins.species.formFiller(), gremlins.species.scroller(), gremlins.species.typer()]," \
         "mogwais: [gremlins.mogwais.alert(), gremlins.mogwais.fps(), gremlins.mogwais.gizmo()]," \
         "strategies: [gremlins.strategies.distribution(), gremlins.strategies.allTogether(), gremlins.strategies.bySpecies()]" \
         "}).unleash();}" \
         "var s = document.createElement(\"script\");" \
         "s.src =  \"https://unpkg.com/gremlins.js\";" \
         "if((s.addEventListener){" \
         "s.addEventListener(\"load\", callback,false);}" \
         "else if (s.readyState) {" \
         "s.onreadystatechange = callback;}" \
         "document.body.appendChild(s);" \
         "})()"

driver.execute_async_script(script)
