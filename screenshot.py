import scrapy
from scrapy.selector import Selector
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.proxy import Proxy, ProxyType
from webdriver_manager.chrome import ChromeDriverManager

class ScreenshotSpider(scrapy.Spider):
    """
    Spider for taking screenshots using Selenium and Scrapy.
    """

    name = "scooty_tor"

    def start_requests(self):
        # Your proxy address
        PROXY = "http://127.0.0.1:8118"

        # Create a Proxy object
        webdriver_service = Service(ChromeDriverManager().install())
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--proxy-server=%s' % PROXY)
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')

        # Start WebDriver with Proxy
        self.driver=webdriver.Chrome(service=webdriver_service, options=chrome_options)
        urls = [
                'http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion',
            ]
        for url in urls:
           yield scrapy.Request(url=url, callback=self.parse, meta={'proxy': PROXY})

    def parse(self, response):
        with open("screenshot.png", "wb") as f:
            self.driver.get(response.url)
            screenshot = self.driver.get_screenshot_as_png()
            f.write(screenshot)



