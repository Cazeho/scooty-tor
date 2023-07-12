import scrapy
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings

class MySpider(scrapy.Spider):
    name = 'scooty_tor'
    start_urls = ['http://']

    def start_requests(self):
        proxy = 'http://localhost:8118'  # Replace with your proxy address
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, meta={'proxy': proxy})

    def parse(self, response):
#        with open('page.html', 'wb') as file:
#            file.write(response.body)

        # Add your scraping logic here
        # For demonstration purposes, we're just printing the page title
        title = response.css('title::text').get()
        print("Page title:", title)
        for link in response.css('a::attr(href)').getall():
            yield {
                'link': link
            }
