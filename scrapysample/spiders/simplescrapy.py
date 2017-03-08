import scrapy
import unicodedata

class SampleSpider(scrapy.Spider):

    name = 'samplespider'
    
    def start_requests(self):
        urls = [
            self.main_site + 'https://www.steelbb.com/pt/steelprices/'
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = '%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)
        products = response.css("table.trackerPricesTable").xpath('//td/text()') 
        for product in products:
             cleaned = product.extract().strip()
             if(cleaned != None and cleaned != ''):
                  print(cleaned)

