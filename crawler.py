import scrapy
from scrapy.exporters import JsonLinesItemExporter
from article_urls import ARTICLES

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ARTICLES

    def parse(self, response):
        for quote in response.css('body'):
            yield {
                'text': quote.css('div').extract_first()
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
        print(self.start_urls)
