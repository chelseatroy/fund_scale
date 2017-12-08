import json, requests
from constants import NEWS_API_KEY
from sp500_service import COMPANY_NAMES

def find_articles_about(company):
    url = ("https://newsapi.org/v2/everything?q=" + company + "&sources=ars-technica&apiKey=" + NEWS_API_KEY)
    response = requests.get(url)
    articles = json.loads(response.text)['articles']

    article_urls = list(map(lambda x: x["url"], articles))
    return article_urls

bunched_articles = []

for company in COMPANY_NAMES:
    bunched_articles.append(find_articles_about(company))

ARTICLES = [item for items in bunched_articles for item in items]

