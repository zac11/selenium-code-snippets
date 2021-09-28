from seleniumwire import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.service import Service

svc=  Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=svc)
driver.maximize_window()
# To use firefox browser
driver.get("https://epco.taleo.net/careersection/alljobs/jobsearch.ftl?lang=en")
for request in driver.requests:
    if request.response:
        print(
            request.url,
            request.response.status_code,
            request.headers,
            request.response.headers

        )