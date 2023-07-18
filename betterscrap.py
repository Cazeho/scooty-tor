import requests as rq
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from seleniumwire import webdriver
from seleniumwire import webdriver as wire_driver
from seleniumwire.thirdparty.mitmproxy.exceptions import TcpException

seleniumwire_options = {
    'verify_ssl': False,
    'suppress_connection_errors': False   # Bypass SSL verification
}


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
driver = wire_driver.Chrome(seleniumwire_options=seleniumwire_options,options=options)

driver.implicitly_wait(15)
url="https://utilimixfr.com"
del driver.requests
try:
    driver.get("https://utilimixfr.com")
except TcpException as e:
    print(str(e))



driver.get(url)
driver.implicitly_wait(30)

with open("logs.txt","w") as f:
    for request in driver.requests:
        f.write(request.url+'\n')
        f.write(str(request.body)+'\n')
