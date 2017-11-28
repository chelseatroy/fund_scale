import scrapy
from scrapy.exporters import JsonLinesItemExporter
from article_urls import ARTICLES

class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = ARTICLES
    url_index = 0

    def parse(self, response):
        for html_text in response.css('body'):
            yield {
                'url': self.start_urls[self.url_index],
                'text': html_text.css('div').extract_first()
            }

        next_page = response.css('li.next a::attr("href")').extract_first()
        if next_page is not None:
            self.url_index = self.url_index + 1
            yield response.follow(next_page, self.parse)
        print(self.start_urls)
