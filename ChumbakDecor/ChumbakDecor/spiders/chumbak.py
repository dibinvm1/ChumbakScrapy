import scrapy
import json


class ChumbakDecoreSpider(scrapy.Spider):
    name = "decor"
    def start_requests(self):
      url='https://api-cdn.chumbak.com/v1/category/920/products?page=1'
      yield scrapy.Request(url=url, callback=self.parse)


    def parse(self, response):
        jresponse = json.loads(response.body_as_unicode())
        last_page = jresponse['product_pages']['num_pages']
        current_page = jresponse['product_pages']['current_page']
        products = jresponse['products']
        print(json.dumps(products, indent=2))
        if current_page  < last_page:
          url = 'https://api-cdn.chumbak.com/v1/category/920/products?page={0}'.format(current_page+1)
          yield scrapy.Request(url,callback=self.parse)
