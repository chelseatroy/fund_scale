python sp500_service.py
python article_urls.py

DATE=`date +%Y-%m-%d`
scrapy runspider crawler.py -o archives/article_text_${DATE}.json
